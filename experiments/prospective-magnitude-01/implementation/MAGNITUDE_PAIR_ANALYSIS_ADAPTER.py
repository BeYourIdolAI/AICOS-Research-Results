import argparse, hashlib, json
from collections import Counter
from pathlib import Path
from MAGNITUDE_ANALYSIS import analyze_pairs

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def rows(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def adapt(plan,scores,analysis_sha,scores_sha,plan_sha):
    planned=plan['trials']; smap={x['trial_id']:x for x in scores}
    if len(planned)!=120 or len(scores)!=120 or len(smap)!=120: raise ValueError('TRIAL_COUNT_INVALID')
    if set(smap)!={x['trial_id'] for x in planned}: raise ValueError('TRIAL_SET_MISMATCH')
    grouped={}
    for p in planned:
        s=smap[p['trial_id']]
        for k in ('trial_id','pair_id','condition'):
            if s[k]!=p[k]: raise ValueError(f'{k.upper()}_MISMATCH')
        pair=grouped.setdefault(p['pair_id'],{"pair_id":p['pair_id']})
        if p['condition'] in pair: raise ValueError('DUPLICATE_CONDITION')
        pair[p['condition']]={"primary_outcome":s['primary_class']}
    if len(grouped)!=60 or any(set(x)!={"pair_id","SMALLER_NOTE","LARGER_NOTE"} for x in grouped.values()): raise ValueError('PAIR_ASSEMBLY_INVALID')
    frozen=analyze_pairs(list(grouped.values())); pc=frozen['pair_class_counts']; effect=frozen['PRIMARY_DESCRIPTIVE_EFFECT']
    primary_counts=Counter(x['primary_class'] for x in scores); basis_counts=Counter(x.get('basis_class') for x in scores)
    anomalies=[{"trial_id":x['trial_id'],"pair_id":x['pair_id'],"condition":x['condition'],"primary_class":x['primary_class'],"basis_class":x.get('basis_class')} for x in scores if x.get('source_attribution_consistent') is False]
    return {"experiment_id":"PROSPECTIVE-MAGNITUDE-01","analysis_logic_sha256":analysis_sha,"scores_sha256":scores_sha,"execution_plan_sha256":plan_sha,"complete_pair_count":frozen['complete_pair_count'],"incomplete_pair_count":frozen['incomplete_pair_count'],"pair_class_counts":{"AUTH_TO_NOTE":pc['AUTH→NOTE'],"NOTE_TO_AUTH":pc['NOTE→AUTH'],"AUTH_TO_AUTH":pc['AUTH→AUTH'],"NOTE_TO_NOTE":pc['NOTE→NOTE']},"primary_descriptive_effect":None if effect=='NOT_COMPUTABLE' else effect,"primary_descriptive_effect_frozen_value":effect,"other_value_trial_count":primary_counts['OTHER_VALUE'],"invalid_format_trial_count":primary_counts['INVALID_FORMAT'],"no_terminal_response_trial_count":primary_counts['NO_TERMINAL_RESPONSE'],"basis_secondary_summary":{"basis_class_counts":dict(basis_counts),"source_attribution_anomaly_count":len(anomalies),"source_attribution_anomalies":anomalies},"incomplete_pairs":frozen['incomplete_pairs'],"frozen_analysis_output":frozen}

def run(plan_path,scores_path,analysis_path,out_path):
    out=adapt(json.loads(plan_path.read_text(encoding='utf-8')),rows(scores_path),sha(analysis_path),sha(scores_path),sha(plan_path)); out_path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n'); return out

def self_test():
    outcomes=[('AUTH_SELECTION','NOTE_SELECTION','AUTH_TO_NOTE'),('NOTE_SELECTION','AUTH_SELECTION','NOTE_TO_AUTH'),('AUTH_SELECTION','AUTH_SELECTION','AUTH_TO_AUTH'),('NOTE_SELECTION','NOTE_SELECTION','NOTE_TO_NOTE')]
    frozen_key={'AUTH_TO_NOTE':'AUTH→NOTE','NOTE_TO_AUTH':'NOTE→AUTH','AUTH_TO_AUTH':'AUTH→AUTH','NOTE_TO_NOTE':'NOTE→NOTE'}
    pairs=[]
    for i,(a,b,key) in enumerate(outcomes): pairs.append({"pair_id":str(i),"SMALLER_NOTE":{"primary_outcome":a},"LARGER_NOTE":{"primary_outcome":b}}); assert analyze_pairs([pairs[-1]])['pair_class_counts'][frozen_key[key]]==1
    incomplete={"pair_id":"x","SMALLER_NOTE":{"primary_outcome":"OTHER_VALUE"},"LARGER_NOTE":{"primary_outcome":"AUTH_SELECTION"}}
    mixed=analyze_pairs(pairs+[incomplete]); assert mixed['complete_pair_count']==4 and mixed['incomplete_pair_count']==1
    zero=analyze_pairs([incomplete]); assert zero['PRIMARY_DESCRIPTIVE_EFFECT']=='NOT_COMPUTABLE'
    plan={"trials":[]}; scores=[]
    for i in range(60):
        pid=f"P-{i:03d}"; a,b,_=outcomes[i%4]
        for condition,primary in [('SMALLER_NOTE',a),('LARGER_NOTE',b)]:
            tid=f"{pid}-{condition}"; plan['trials'].append({"trial_id":tid,"pair_id":pid,"condition":condition}); scores.append({"trial_id":tid,"pair_id":pid,"condition":condition,"primary_class":primary,"basis_class":"AUTH_ATTRIBUTION","source_attribution_consistent":True})
    integrated=adapt(plan,scores,'a'*64,'b'*64,'c'*64); expected=analyze_pairs([{"pair_id":f"P-{i:03d}","SMALLER_NOTE":{"primary_outcome":outcomes[i%4][0]},"LARGER_NOTE":{"primary_outcome":outcomes[i%4][1]}} for i in range(60)])
    assert integrated['frozen_analysis_output']==expected and integrated['complete_pair_count']==60
    zero_scores=[dict(x,primary_class='OTHER_VALUE',basis_class='OTHER_ATTRIBUTION',source_attribution_consistent=None) for x in scores]
    zero_integrated=adapt(plan,zero_scores,'a'*64,'b'*64,'c'*64); assert zero_integrated['complete_pair_count']==0 and zero_integrated['primary_descriptive_effect'] is None and zero_integrated['primary_descriptive_effect_frozen_value']=='NOT_COMPUTABLE'
    return {"status":"PASS","cases":["AUTH→NOTE","NOTE→AUTH","AUTH→AUTH","NOTE→NOTE","incomplete pair","zero complete pairs","120-score pair adapter integration"],"target_called":False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--plan',type=Path); ap.add_argument('--scores',type=Path); ap.add_argument('--analysis-logic',type=Path); ap.add_argument('--out',type=Path); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args()
    if a.self_test: print(json.dumps(self_test(),ensure_ascii=False,indent=2)); return
    if not all((a.plan,a.scores,a.analysis_logic,a.out)): ap.error('execution mode requires --plan --scores --analysis-logic --out')
    run(a.plan,a.scores,a.analysis_logic,a.out)
if __name__=='__main__': main()
