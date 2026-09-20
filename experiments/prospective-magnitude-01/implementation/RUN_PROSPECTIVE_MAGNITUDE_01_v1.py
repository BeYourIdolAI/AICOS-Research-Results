import argparse, base64, hashlib, json, os, re, subprocess, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

EXPERIMENT_ID="PROSPECTIVE-MAGNITUDE-01"
EXPECTED={
"PROSPECTIVE-MAGNITUDE-01_v0.1_FROZEN.md":"9bab675eb157a51091c3c20a11304d62150e01b42c74850c46e3f8f14912c48f","MAGNITUDE_CORPUS_GENERATOR.py":"ce9ddb1a3f11521cb862ca5e8fc77f24f812458d9683d81b32701978316cd6f3","MAGNITUDE_CORPUS_GENERATION_LOG.json":"e268b89393cdd7c3f7cae73839e68bb4a94b3df00cf5c64ce821b8adc3fb342d","MAGNITUDE_CORPUS_MANIFEST.json":"ae5995373a474450991dceac187dc38f233a4fcc1578c96c4b94fc70bcda0b50","MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json":"c8cf2e18efeb051564ded2b411572c69f5a6efd8457f32be5c4a24a81672af25","MAGNITUDE_PARSER_SCORER.py":"2dd8bf7b1fc2c4183b35c666998dc45da56f429f0c2c8a854b0ea93ea9985712","MAGNITUDE_ANALYSIS.py":"ffb03a70321eb8e422251348844a9dc2108b5e46e0b5607a6962d6557d9fa650","MAGNITUDE_EXECUTION_PLAN.json":"f8f62f5d976b958d6d93550dbb3bd6affe8f92111c2b1fa5ef3e0f588dd328b7","MAGNITUDE_FINAL_FREEZE_MANIFEST.json":"d25558549c4644043003963c44acd06813a6d3a117c7259c961f2d96cf354215","PROSPECTIVE-MAGNITUDE-01_v0.2_PREOBS_IMPLEMENTATION_PATCH.md":"3bb2d08ce9d50b58704f2b9e3c73e7424c670e4a17f9730fe97da5b6fbe20789","MAGNITUDE_SCORE_ADAPTER.py":"972d18b846e9ac95f9186da4cdc51c217830f125921d1f63c9dcd56364cd38a8","MAGNITUDE_PAIR_ANALYSIS_ADAPTER.py":"a0b04f2b581786f9d85100c9415576c8fb5c134ae543b99fb3eaf1a7a7437a70","PROSPECTIVE-MAGNITUDE-01_v0.2_FREEZE_MANIFEST.json":"6e85cc2f8fec800bc970e2a54191660789f4fea633a12d3a253c5bca3f7df236"}
PREEXEC="MAGNITUDE_RUNNER_PREEXEC_RECORD_v1.json"; RUN_DIR="MAGNITUDE_EXECUTION_001"

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p): return sha_bytes(p.read_bytes())
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def canonical(obj): return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
def utc(): return datetime.now(timezone.utc).isoformat(timespec='microseconds')
def write_json(p,obj): p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def append_jsonl(p,obj):
    with open(p,'ab') as f: f.write(canonical(obj)+b'\n'); f.flush(); os.fsync(f.fileno())

def verify_frozen(root,verify_runtime=True):
    hashes={}
    for name,expected in EXPECTED.items():
        p=root/name
        if not p.is_file(): raise SystemExit(f'STOP: missing frozen artifact: {name}')
        actual=sha_file(p)
        if actual!=expected: raise SystemExit(f'STOP: frozen hash mismatch: {name}: {actual}')
        hashes[name]=actual
    target=load(root/'MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json')
    model=root/target['target']['model_filename']; runtime=root/target['runtime']['binary_relative_path']
    if verify_runtime:
        if not model.is_file() or sha_file(model)!=target['target']['model_sha256']: raise SystemExit('STOP: model identity mismatch')
        if not runtime.is_file() or sha_file(runtime)!=target['runtime']['runtime_binary_sha256']: raise SystemExit('STOP: runtime identity mismatch')
    return hashes,target,model,runtime

def render_request(condition,target):
    records=json.dumps(condition['records'],ensure_ascii=False,sort_keys=True,separators=(',',':'))
    user=target['prompts']['user_prompt_rendering']['exact_template'].format(records_json=records,question=condition['question'])
    system=target['prompts']['system_prompt_exact']; return system,user,canonical({'system_prompt':system,'user_prompt':user})

def validate_design(root,target):
    corpus=load(root/'MAGNITUDE_CORPUS_MANIFEST.json'); plan=load(root/'MAGNITUDE_EXECUTION_PLAN.json')
    if len(corpus['pairs'])!=60 or len(plan['trials'])!=120: raise SystemExit('STOP: pair/trial count invalid')
    pairs={p['pair_id']:p for p in corpus['pairs']}; counts=Counter(x['pair_id'] for x in plan['trials'])
    if len(pairs)!=60 or len(counts)!=60 or set(counts.values())!={2}: raise SystemExit('STOP: pair coverage invalid')
    for i,p in enumerate(corpus['pairs'],1):
        if not p['smaller_value']<p['larger_value']: raise SystemExit('STOP: magnitude ordering invalid')
        s,l=p['SMALLER_NOTE'],p['LARGER_NOTE']
        if s['records'][0]['value']!=p['larger_value'] or s['records'][1]['value']!=p['smaller_value'] or l['records'][0]['value']!=p['smaller_value'] or l['records'][1]['value']!=p['larger_value']: raise SystemExit('STOP: numeric mirror invalid')
        for c in (s,l):
            if [x['record_type'] for x in c['records']]!=['AUTHORITATIVE_RECORD','SECONDARY_NOTE'] or c['records'][1].get('verification_status')!='UNVERIFIED': raise SystemExit('STOP: record order/status invalid')
        planned=[x for x in plan['trials'] if x['pair_id']==p['pair_id']]; expected=['SMALLER_NOTE','LARGER_NOTE'] if i%2 else ['LARGER_NOTE','SMALLER_NOTE']
        if [x['condition'] for x in planned]!=expected: raise SystemExit('STOP: execution order invalid')
        for x in planned:
            c=p[x['condition']]
            if x['item_id']!=c['item_id'] or x['trial_id']!=f"{p['pair_id']}-{x['condition']}": raise SystemExit('STOP: plan/corpus mapping invalid')
            _,_,rb=render_request(c,target)
            if x['request_sha256']!=sha_bytes(rb) or base64.b64decode(x['request_b64'],validate=True)!=rb: raise SystemExit('STOP: frozen request identity invalid')
    return corpus,plan,pairs

def preexec_object(runner_path):
    return {"experiment_id":EXPERIMENT_ID,"record_type":"RUNNER_PREEXEC_RECORD","observation_performed":False,"experiment_execution":False,"runner_filename":runner_path.name,"runner_sha256":sha_file(runner_path),"v0_1_final_freeze_manifest_sha256":EXPECTED['MAGNITUDE_FINAL_FREEZE_MANIFEST.json'],"v0_2_freeze_manifest_sha256":EXPECTED['PROSPECTIVE-MAGNITUDE-01_v0.2_FREEZE_MANIFEST.json'],"corpus_manifest_sha256":EXPECTED['MAGNITUDE_CORPUS_MANIFEST.json'],"execution_plan_sha256":EXPECTED['MAGNITUDE_EXECUTION_PLAN.json'],"target_configuration_sha256":EXPECTED['MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json'],"parser_scorer_sha256":EXPECTED['MAGNITUDE_PARSER_SCORER.py'],"analysis_sha256":EXPECTED['MAGNITUDE_ANALYSIS.py'],"score_adapter_sha256":EXPECTED['MAGNITUDE_SCORE_ADAPTER.py'],"pair_analysis_adapter_sha256":EXPECTED['MAGNITUDE_PAIR_ANALYSIS_ADAPTER.py'],"planned_pair_count":60,"planned_trial_count":120}

def do_preflight(root):
    _,target,_,_=verify_frozen(root,True); validate_design(root,target)
    if (root/RUN_DIR).exists(): raise SystemExit(f'STOP: {RUN_DIR} already exists')
    p=root/PREEXEC
    if p.exists(): raise SystemExit(f'STOP: {PREEXEC} already exists; refusing overwrite')
    write_json(p,preexec_object(Path(__file__).resolve()))
    print(f'PREEXEC SHA256: {sha_file(p)}'); print('PREFLIGHT PASS — NO TARGET TRIAL EXECUTED.')

def extract(stdout,user):
    text=stdout.decode('utf-8','strict'); pattern=re.compile(''.join(r'(?:\r?\n)' if c=='\n' else re.escape(c) for c in user)); matches=list(pattern.finditer(text))
    if len(matches)!=1: raise ValueError(f'FROZEN_USER_PROMPT_MATCH_COUNT_{len(matches)}_EXPECTED_1')
    tail=text[matches[0].end():]; pos=0 if tail.startswith('[ Prompt:') else None
    if pos is None:
        for i,c in enumerate(tail):
            if c in '\r\n' and tail.startswith('[ Prompt:',i+1): pos=i+1; break
    if pos is None: raise ValueError('PROMPT_FOOTER_LINE_NOT_FOUND')
    return tail[:pos].strip('\r\n').encode('utf-8')

def invoke(runtime,model,target,system,user):
    ec=target['execution_configuration']; cmd=[str(runtime),'--model',str(model),'--ctx-size',str(ec['context_length']),'--predict',str(ec['max_output_tokens']),'--seed',str(ec['seed']),'--temperature',str(ec['temperature']),'--top-p',str(ec['top_p']),'--system-prompt',system,'--prompt',user,'--simple-io','--single-turn','--no-display-prompt','--color','off']; start=utc()
    try:
        p=subprocess.run(cmd,cwd=str(runtime.parent),stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False); end=utc()
        if p.stdout:
            try: response_bytes=extract(p.stdout,user); return {"start":start,"end":end,"terminal":True,"infra":None,"extract":None,"response":response_bytes,"stdout":p.stdout,"stderr":p.stderr,"returncode":p.returncode}
            except ValueError as e: return {"start":start,"end":end,"terminal":False,"infra":None,"extract":str(e),"response":None,"stdout":p.stdout,"stderr":p.stderr,"returncode":p.returncode}
        return {"start":start,"end":end,"terminal":False,"infra":f'NO_TERMINAL_STDOUT_RETURN_CODE_{p.returncode}',"extract":None,"response":None,"stdout":p.stdout,"stderr":p.stderr,"returncode":p.returncode}
    except Exception as e: return {"start":start,"end":utc(),"terminal":False,"infra":f'{type(e).__name__}: {e}',"extract":None,"response":None,"stdout":b'',"stderr":b'',"returncode":None}

def make_attempt(trial_id,n,request,result):
    response_bytes=result['response']; return {"attempt_id":f'{trial_id}-A{n}',"request_b64":base64.b64encode(request).decode(),"request_sha256":sha_bytes(request),"response_b64":None if response_bytes is None else base64.b64encode(response_bytes).decode(),"response_sha256":None if response_bytes is None else sha_bytes(response_bytes),"terminal_delivered":result['terminal'],"infrastructure_error":result['infra'],"start_timestamp":result['start'],"end_timestamp":result['end']}

def log_attempt(path,trial,attempt,result):
    append_jsonl(path,{"trial_id":trial['trial_id'],"pair_id":trial['pair_id'],"condition":trial['condition'],"attempt_id":attempt['attempt_id'],"request_sha256":attempt['request_sha256'],"response_sha256":attempt['response_sha256'],"raw_stdout_b64":base64.b64encode(result['stdout']).decode(),"raw_stdout_sha256":sha_bytes(result['stdout']),"extraction_error":result['extract'],"stderr_b64":base64.b64encode(result['stderr']).decode(),"stderr_sha256":sha_bytes(result['stderr']),"process_returncode":result['returncode'],"terminal_delivered":attempt['terminal_delivered'],"infrastructure_error":attempt['infrastructure_error'],"start_timestamp":attempt['start_timestamp'],"end_timestamp":attempt['end_timestamp']})

def do_run(root):
    _,target,model,runtime=verify_frozen(root,True); corpus,plan,pairs=validate_design(root,target); prepath=root/PREEXEC
    if not prepath.is_file(): raise SystemExit('STOP: preexec record missing')
    pre=load(prepath); runner_sha=sha_file(Path(__file__).resolve())
    if pre.get('runner_sha256')!=runner_sha or pre.get('execution_plan_sha256')!=EXPECTED['MAGNITUDE_EXECUTION_PLAN.json'] or pre.get('v0_2_freeze_manifest_sha256')!=EXPECTED['PROSPECTIVE-MAGNITUDE-01_v0.2_FREEZE_MANIFEST.json']: raise SystemExit('STOP: preexec identity mismatch')
    rundir=root/RUN_DIR
    if rundir.exists(): raise SystemExit(f'STOP: {RUN_DIR} already exists')
    rundir.mkdir(); started=utc()
    exec_record={"experiment_id":EXPERIMENT_ID,"execution_start_timestamp":started,"runner_sha256":runner_sha,"preexec_record_sha256":sha_file(prepath),"v0_1_final_freeze_manifest_sha256":EXPECTED['MAGNITUDE_FINAL_FREEZE_MANIFEST.json'],"v0_2_freeze_manifest_sha256":EXPECTED['PROSPECTIVE-MAGNITUDE-01_v0.2_FREEZE_MANIFEST.json'],"corpus_sha256":EXPECTED['MAGNITUDE_CORPUS_MANIFEST.json'],"execution_plan_sha256":EXPECTED['MAGNITUDE_EXECUTION_PLAN.json'],"target_configuration_sha256":EXPECTED['MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json'],"parser_scorer_sha256":EXPECTED['MAGNITUDE_PARSER_SCORER.py'],"analysis_sha256":EXPECTED['MAGNITUDE_ANALYSIS.py'],"score_adapter_sha256":EXPECTED['MAGNITUDE_SCORE_ADAPTER.py'],"pair_analysis_adapter_sha256":EXPECTED['MAGNITUDE_PAIR_ANALYSIS_ADAPTER.py'],"model_sha256":target['target']['model_sha256'],"llama_cli_sha256":target['runtime']['runtime_binary_sha256']}; write_json(rundir/'EXECUTION_RECORD.json',exec_record)
    rawp=rundir/'RAW.jsonl'; logp=rundir/'LOGS.jsonl'
    for trial in plan['trials']:
        condition=pairs[trial['pair_id']][trial['condition']]; system,user,request=render_request(condition,target)
        if sha_bytes(request)!=trial['request_sha256'] or base64.b64encode(request).decode()!=trial['request_b64']: raise SystemExit('STOP: request differs from frozen plan')
        attempts=[]; result=invoke(runtime,model,target,system,user); attempt=make_attempt(trial['trial_id'],1,request,result); attempts.append(attempt); log_attempt(logp,trial,attempt,result)
        if not result['terminal'] and result['infra'] is not None:
            result=invoke(runtime,model,target,system,user); attempt=make_attempt(trial['trial_id'],2,request,result); attempts.append(attempt); log_attempt(logp,trial,attempt,result)
        append_jsonl(rawp,{"trial_id":trial['trial_id'],"pair_id":trial['pair_id'],"condition":trial['condition'],"target_configuration_sha256":EXPECTED['MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json'],"attempts":attempts})
    if len(rawp.read_bytes().splitlines())!=120: raise SystemExit('STOP: RAW count invalid')
    scores=rundir/'SCORES.jsonl'; analysis=rundir/'ANALYSIS.json'
    subprocess.run([sys.executable,str(root/'MAGNITUDE_SCORE_ADAPTER.py'),'--plan',str(root/'MAGNITUDE_EXECUTION_PLAN.json'),'--corpus',str(root/'MAGNITUDE_CORPUS_MANIFEST.json'),'--raw',str(rawp),'--target-config-sha256',EXPECTED['MAGNITUDE_TARGET_CONFIGURATION_MANIFEST.json'],'--out',str(scores)],cwd=str(root),check=True)
    subprocess.run([sys.executable,str(root/'MAGNITUDE_PAIR_ANALYSIS_ADAPTER.py'),'--plan',str(root/'MAGNITUDE_EXECUTION_PLAN.json'),'--scores',str(scores),'--analysis-logic',str(root/'MAGNITUDE_ANALYSIS.py'),'--out',str(analysis)],cwd=str(root),check=True)
    score_rows=[json.loads(x) for x in scores.read_text(encoding='utf-8').splitlines() if x.strip()]
    if len(score_rows)!=120 or len({x['trial_id'] for x in score_rows})!=120 or {x['trial_id'] for x in score_rows}!={x['trial_id'] for x in plan['trials']}: raise SystemExit('STOP: final score integrity invalid')
    verify_frozen(root,False); a=load(analysis); pc=a['pair_class_counts']
    print('RUN COMPLETE. Frozen scoring and paired analysis complete.\n'); print(f"PRIMARY DESCRIPTIVE EFFECT: {a['primary_descriptive_effect_frozen_value']}"); print(f"COMPLETE PAIRS: {a['complete_pair_count']}\nINCOMPLETE PAIRS: {a['incomplete_pair_count']}\n"); print(f"AUTH→NOTE: {pc['AUTH_TO_NOTE']}\nNOTE→AUTH: {pc['NOTE_TO_AUTH']}\nAUTH→AUTH: {pc['AUTH_TO_AUTH']}\nNOTE→NOTE: {pc['NOTE_TO_NOTE']}\n"); print(f"OTHER_VALUE TRIALS: {a['other_value_trial_count']}\nINVALID_FORMAT TRIALS: {a['invalid_format_trial_count']}\nNO_TERMINAL_RESPONSE TRIALS: {a['no_terminal_response_trial_count']}\n"); print(f"RAW SHA256: {sha_file(rawp)}\nLOGS SHA256: {sha_file(logp)}\nSCORES SHA256: {sha_file(scores)}\nANALYSIS SHA256: {sha_file(analysis)}\nEXECUTION RECORD SHA256: {sha_file(rundir/'EXECUTION_RECORD.json')}\n\nSTOP HERE.")

def main():
    ap=argparse.ArgumentParser(); modes=ap.add_mutually_exclusive_group(required=True); modes.add_argument('--preflight',action='store_true'); modes.add_argument('--run',action='store_true'); a=ap.parse_args(); root=Path(__file__).resolve().parent
    if a.preflight: do_preflight(root)
    else: do_run(root)
if __name__=='__main__': main()
