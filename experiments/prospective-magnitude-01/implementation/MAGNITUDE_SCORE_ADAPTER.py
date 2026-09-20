import argparse, base64, hashlib, json, tempfile
from pathlib import Path
from MAGNITUDE_PARSER_SCORER import score_trial, response

TRIAL_KEYS={"trial_id","pair_id","condition","target_configuration_sha256","attempts"}
ATTEMPT_KEYS={"attempt_id","request_b64","request_sha256","response_b64","response_sha256","terminal_delivered","infrastructure_error","start_timestamp","end_timestamp"}

def sha(b): return hashlib.sha256(b).hexdigest()
def rows(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def write_rows(path,data): path.write_text(''.join(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n' for x in data),encoding='utf-8',newline='\n')

def select_attempt(trial):
    attempts=trial['attempts']
    if len(attempts) not in (1,2): raise ValueError('ATTEMPT_COUNT_INVALID')
    for a in attempts:
        if set(a)!=ATTEMPT_KEYS: raise ValueError('ATTEMPT_FIELDS_MISMATCH')
        rb=base64.b64decode(a['request_b64'],validate=True)
        if sha(rb)!=a['request_sha256']: raise ValueError('REQUEST_HASH_MISMATCH')
    if len(attempts)==2:
        if attempts[0]['terminal_delivered'] or not attempts[0]['infrastructure_error']: raise ValueError('RETRY_NOT_QUALIFYING')
        if attempts[0]['request_b64']!=attempts[1]['request_b64'] or attempts[0]['request_sha256']!=attempts[1]['request_sha256']: raise ValueError('RETRY_INPUT_CHANGED')
    terminals=[a for a in attempts if a['terminal_delivered']]
    if len(terminals)>1: raise ValueError('MULTIPLE_TERMINAL_ATTEMPTS')
    chosen=terminals[0] if terminals else attempts[-1]
    if chosen['terminal_delivered']:
        if chosen['response_b64'] is None or chosen['response_sha256'] is None: raise ValueError('TERMINAL_RESPONSE_MISSING')
        bb=base64.b64decode(chosen['response_b64'],validate=True)
        if sha(bb)!=chosen['response_sha256']: raise ValueError('RESPONSE_HASH_MISMATCH')
    elif chosen['response_b64'] is not None or chosen['response_sha256'] is not None:
        raise ValueError('NONTERMINAL_RESPONSE_PRESENT')
    return chosen

def adapt(plan,corpus,raw_trials,target_sha):
    planned=plan['trials']; pmap={x['trial_id']:x for x in planned}; pairs={x['pair_id']:x for x in corpus['pairs']}
    if len(planned)!=120 or len(pmap)!=120 or len(raw_trials)!=120: raise ValueError('TRIAL_COUNT_INVALID')
    rmap={x['trial_id']:x for x in raw_trials}
    if set(rmap)!=set(pmap): raise ValueError('TRIAL_SET_MISMATCH')
    out=[]
    for p in planned:
        t=rmap[p['trial_id']]
        if set(t)!=TRIAL_KEYS: raise ValueError('RAW_FIELDS_MISMATCH')
        for k in ('trial_id','pair_id','condition'):
            if t[k]!=p[k]: raise ValueError(f'{k.upper()}_MISMATCH')
        if t['target_configuration_sha256']!=target_sha: raise ValueError('TARGET_CONFIG_MISMATCH')
        chosen=select_attempt(t); cond=pairs[t['pair_id']][t['condition']]
        frozen=score_trial(chosen['response_b64'],cond,chosen['terminal_delivered'])
        primary=frozen['primary_outcome']; basis_class=frozen.get('attribution')
        consistent=None if primary not in ('AUTH_SELECTION','NOTE_SELECTION') else not frozen.get('source_attribution_anomaly',False)
        rec={"trial_id":t['trial_id'],"pair_id":t['pair_id'],"condition":t['condition'],"primary_class":primary,"returned_value":frozen.get('returned_value'),"basis_id":frozen.get('basis_id'),"basis_class":basis_class,"source_attribution_consistent":consistent,"source_raw_response_sha256":chosen['response_sha256'] if chosen['terminal_delivered'] else None,"frozen_scorer_output":frozen}
        out.append(rec)
    return out

def run(plan_path,corpus_path,raw_path,target_sha,out_path):
    result=adapt(json.loads(plan_path.read_text(encoding='utf-8')),json.loads(corpus_path.read_text(encoding='utf-8')),rows(raw_path),target_sha); write_rows(out_path,result); return result

def self_test():
    cond={"records":[{"record_id":"AUTH-X","value":9000},{"record_id":"NOTE-X","value":1000}]}
    cases=[('AUTH_SELECTION',response(9000,'AUTH-X'),True),('NOTE_SELECTION',response(1000,'NOTE-X'),True),('OTHER_VALUE',response(5555,'AUTH-X'),True),('INVALID_FORMAT',base64.b64encode(b'bad').decode(),True),('NO_TERMINAL_RESPONSE',None,False),('AUTH_SELECTION',response(9000,'NOTE-X'),True)]
    got=[]
    for expected,b64,terminal in cases:
        frozen=score_trial(b64,cond,terminal); assert frozen['primary_outcome']==expected
        primary=frozen['primary_outcome']; consistent=None if primary not in ('AUTH_SELECTION','NOTE_SELECTION') else not frozen.get('source_attribution_anomaly',False)
        got.append((primary,consistent))
    assert got[-1]==('AUTH_SELECTION',False)
    plan={"trials":[]}; corpus={"pairs":[]}; raw=[]; target='t'*64
    for i in range(60):
        pid=f"P-{i:03d}"; corpus['pairs'].append({"pair_id":pid,"SMALLER_NOTE":cond,"LARGER_NOTE":cond})
        for condition in ('SMALLER_NOTE','LARGER_NOTE'):
            trial_id=f"{pid}-{condition}"; plan['trials'].append({"trial_id":trial_id,"pair_id":pid,"condition":condition})
            rb=b'{}'; response_b64=response(9000,'NOTE-X'); response_bytes=base64.b64decode(response_b64)
            raw.append({"trial_id":trial_id,"pair_id":pid,"condition":condition,"target_configuration_sha256":target,"attempts":[{"attempt_id":trial_id+'-A1',"request_b64":base64.b64encode(rb).decode(),"request_sha256":sha(rb),"response_b64":response_b64,"response_sha256":sha(response_bytes),"terminal_delivered":True,"infrastructure_error":None,"start_timestamp":"s","end_timestamp":"e"}]})
    adapted=adapt(plan,corpus,raw,target); assert len(adapted)==120 and all(x['primary_class']=='AUTH_SELECTION' and x['source_attribution_consistent'] is False for x in adapted)
    return {"status":"PASS","cases":["NOTE_SELECTION","AUTH_SELECTION","OTHER_VALUE","INVALID_FORMAT","NO_TERMINAL_RESPONSE","value/basis attribution mismatch","120-record RAW adapter integration"],"target_called":False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--plan',type=Path); ap.add_argument('--corpus',type=Path); ap.add_argument('--raw',type=Path); ap.add_argument('--target-config-sha256'); ap.add_argument('--out',type=Path); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args()
    if a.self_test: print(json.dumps(self_test(),ensure_ascii=False,indent=2)); return
    if not all((a.plan,a.corpus,a.raw,a.target_config_sha256,a.out)): ap.error('execution mode requires --plan --corpus --raw --target-config-sha256 --out')
    run(a.plan,a.corpus,a.raw,a.target_config_sha256,a.out)
if __name__=='__main__': main()
