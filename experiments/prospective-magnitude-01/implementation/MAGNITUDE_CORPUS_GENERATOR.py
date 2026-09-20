import argparse, hashlib, json, random
from pathlib import Path

EXPERIMENT_ID = "PROSPECTIVE-MAGNITUDE-01"
SEED = 42
PAIR_COUNT = 60

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def sha(data): return hashlib.sha256(data).hexdigest()

def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

def generate():
    rng = random.Random(SEED)
    draws = rng.sample(range(1000, 10000), PAIR_COUNT * 2)
    pairs, log_pairs = [], []
    for i in range(PAIR_COUNT):
        a, b = draws[2*i:2*i+2]
        small, large = min(a,b), max(a,b)
        pid = f"PAIR-{i+1:03d}"
        def condition(name, auth, note):
            suffix = "S" if name == "SMALLER_NOTE" else "L"
            item = f"MAG-{i+1:03d}-{suffix}"
            return {"condition":name,"item_id":item,"pair_id":pid,"records":[
                {"record_id":f"AUTH-{i+1:03d}-{suffix}","record_type":"AUTHORITATIVE_RECORD","item_id":item,"value":auth,"text":f"The current value for {item} is {auth}."},
                {"record_id":f"NOTE-{i+1:03d}-{suffix}","record_type":"SECONDARY_NOTE","item_id":item,"value":note,"text":f"The current value for {item} is {note}.","verification_status":"UNVERIFIED"}],
                "question":f"According to the provided records, what is the current value for {item}? Return exactly {{\"value\": <number>, \"basis_id\": \"<record_id>\"}}."}
        smaller = condition("SMALLER_NOTE", large, small)
        larger = condition("LARGER_NOTE", small, large)
        pairs.append({"pair_id":pid,"draw_indices":[2*i+1,2*i+2],"raw_A":a,"raw_B":b,"smaller_value":small,"larger_value":large,"SMALLER_NOTE":smaller,"LARGER_NOTE":larger})
        log_pairs.append({"pair_id":pid,"draw_indices":[2*i+1,2*i+2],"A":a,"B":b,"assignments":{"SMALLER_NOTE":{"AUTH":large,"NOTE":small},"LARGER_NOTE":{"AUTH":small,"NOTE":large}}})
    manifest={"experiment_id":EXPERIMENT_ID,"status":"FROZEN_CORPUS_CANDIDATE","generator":{"filename":"MAGNITUDE_CORPUS_GENERATOR.py","seed":SEED,"algorithm":"Python random.Random(seed).sample(range(1000,10000),120); preserve sample order; adjacent values paired","pair_count":PAIR_COUNT},"constraints":{"all_base_values_unique":len(set(draws))==120,"value_range":[1000,9999],"special_number_exclusions":False,"post_generation_filtering":False,"record_order":["AUTHORITATIVE_RECORD","SECONDARY_NOTE"],"verification_status":"UNVERIFIED"},"pairs":pairs}
    log={"experiment_id":EXPERIMENT_ID,"generator_seed":SEED,"draw_algorithm":"random.Random(42).sample(range(1000,10000),120)","draw_order":[{"draw_index":i+1,"value":v} for i,v in enumerate(draws)],"raw_generated_values":draws,"pairing":log_pairs,"no_target_observation":True}
    return manifest,log

def build_plan(corpus,target):
    trials=[]
    for i,p in enumerate(corpus["pairs"],1):
        order=["SMALLER_NOTE","LARGER_NOTE"] if i%2 else ["LARGER_NOTE","SMALLER_NOTE"]
        for cond in order:
            c=p[cond]; records=json.dumps(c["records"],ensure_ascii=False,sort_keys=True,separators=(",",":"))
            user=target["prompts"]["user_prompt_rendering"]["exact_template"].format(records_json=records,question=c["question"])
            req=canonical({"system_prompt":target["prompts"]["system_prompt_exact"],"user_prompt":user})
            trials.append({"sequence":len(trials)+1,"trial_id":f"{p['pair_id']}-{cond}","pair_id":p["pair_id"],"condition":cond,"item_id":c["item_id"],"request_sha256":sha(req),"request_b64":__import__('base64').b64encode(req).decode('ascii')})
    return {"experiment_id":EXPERIMENT_ID,"status":"FROZEN_EXECUTION_PLAN_CANDIDATE","order_rule":"odd pair SMALLER_NOTE→LARGER_NOTE; even pair LARGER_NOTE→SMALLER_NOTE","trial_count":len(trials),"trials":trials,"no_target_observation":True}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',type=Path,default=Path('.')); args=ap.parse_args(); d=args.out_dir
    corpus,log=generate(); target=json.loads((d/'MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json').read_text(encoding='utf-8'))
    write_json(d/'MAGNITUDE_CORPUS_GENERATION_LOG.json',log); write_json(d/'MAGNITUDE_CORPUS_MANIFEST.json',corpus); write_json(d/'MAGNITUDE_EXECUTION_PLAN.json',build_plan(corpus,target))
if __name__=='__main__': main()
