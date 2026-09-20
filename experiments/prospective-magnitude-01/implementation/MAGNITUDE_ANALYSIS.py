import argparse, json, tempfile
from pathlib import Path
from MAGNITUDE_PARSER_SCORER import score_trial,response

PAIR_CLASSES={("AUTH_SELECTION","NOTE_SELECTION"):"AUTH→NOTE",("NOTE_SELECTION","AUTH_SELECTION"):"NOTE→AUTH",("AUTH_SELECTION","AUTH_SELECTION"):"AUTH→AUTH",("NOTE_SELECTION","NOTE_SELECTION"):"NOTE→NOTE"}

def analyze_pairs(pairs):
    counts={x:0 for x in ("AUTH→NOTE","NOTE→AUTH","AUTH→AUTH","NOTE→NOTE")}; incomplete=[]
    for p in pairs:
        a=p["SMALLER_NOTE"]["primary_outcome"]; b=p["LARGER_NOTE"]["primary_outcome"]
        cls=PAIR_CLASSES.get((a,b))
        if cls: counts[cls]+=1
        else: incomplete.append({"pair_id":p["pair_id"],"SMALLER_NOTE":a,"LARGER_NOTE":b,"reason":"one or both conditions not AUTH_SELECTION/NOTE_SELECTION"})
    complete=sum(counts.values()); effect=None if complete==0 else (counts["AUTH→NOTE"]-counts["NOTE→AUTH"])/complete
    return {"planned_pair_count":len(pairs),"complete_pair_count":complete,"incomplete_pair_count":len(incomplete),"incomplete_pairs":incomplete,"pair_class_counts":counts,"PRIMARY_DESCRIPTIVE_EFFECT":"NOT_COMPUTABLE" if effect is None else effect}

def fixture():
    return {"records":[{"record_id":"AUTH-X","value":9000},{"record_id":"NOTE-X","value":1000}]}

def self_test():
    c=fixture(); A=lambda outcome,basis="AUTH-X": score_trial(response(9000 if outcome=="AUTH" else 1000,basis),c)
    classes=[("AUTH","NOTE","AUTH→NOTE"),("NOTE","AUTH","NOTE→AUTH"),("AUTH","AUTH","AUTH→AUTH"),("NOTE","NOTE","NOTE→NOTE")]
    pairs=[]
    for i,(x,y,z) in enumerate(classes):
        p={"pair_id":str(i),"SMALLER_NOTE":A(x),"LARGER_NOTE":A(y)}; assert analyze_pairs([p])["pair_class_counts"][z]==1; pairs.append(p)
    other=score_trial(response(5555,"AUTH-X"),c); malformed=score_trial(__import__('base64').b64encode(b'not json').decode(),c); none=score_trial(None,c,False)
    assert other["primary_outcome"]=="OTHER_VALUE" and malformed["primary_outcome"]=="INVALID_FORMAT" and none["primary_outcome"]=="NO_TERMINAL_RESPONSE"
    inconsistent=score_trial(response(9000,"NOTE-X"),c); assert inconsistent["primary_outcome"]=="AUTH_SELECTION" and inconsistent["source_attribution_anomaly"]
    zero=analyze_pairs([{"pair_id":"z","SMALLER_NOTE":other,"LARGER_NOTE":malformed}]); assert zero["PRIMARY_DESCRIPTIVE_EFFECT"]=="NOT_COMPUTABLE"
    mixed=analyze_pairs(pairs+[{"pair_id":"m","SMALLER_NOTE":other,"LARGER_NOTE":none}]); assert mixed["complete_pair_count"]==4 and mixed["incomplete_pair_count"]==1 and mixed["PRIMARY_DESCRIPTIVE_EFFECT"]==0
    directional=analyze_pairs([pairs[0],pairs[0],pairs[1]]); assert directional["PRIMARY_DESCRIPTIVE_EFFECT"]==(2-1)/3
    return {"status":"PASS","cases":["AUTH→NOTE","NOTE→AUTH","AUTH→AUTH","NOTE→NOTE","OTHER_VALUE","malformed JSON","no terminal response","value/basis inconsistency","zero complete pairs","mixed complete/incomplete pairs","effect formula"],"target_called":False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    if args.self_test: print(json.dumps(self_test(),indent=2,ensure_ascii=False))
if __name__=='__main__': main()
