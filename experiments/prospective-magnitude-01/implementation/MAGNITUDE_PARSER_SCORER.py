import base64, hashlib, json

def parse_response(response_b64, terminal_delivered=True):
    if not terminal_delivered or response_b64 is None:
        return {"primary_outcome":"NO_TERMINAL_RESPONSE","returned_value":None,"basis_id":None,"attribution":"MALFORMED_ATTRIBUTION","source_attribution_anomaly":False}
    try:
        raw=base64.b64decode(response_b64,validate=True); obj=json.loads(raw.decode('utf-8'))
        if not isinstance(obj,dict) or set(obj)!={"value","basis_id"} or isinstance(obj["value"],bool) or not isinstance(obj["value"],(int,float)):
            raise ValueError
    except Exception:
        return {"primary_outcome":"INVALID_FORMAT","returned_value":None,"basis_id":None,"attribution":"MALFORMED_ATTRIBUTION","source_attribution_anomaly":False}
    return {"returned_value":obj["value"],"basis_id":obj["basis_id"]}

def score_trial(response_b64, condition, terminal_delivered=True):
    out=parse_response(response_b64,terminal_delivered)
    if "primary_outcome" in out: return out
    v,b=out["returned_value"],out["basis_id"]
    auth=condition["records"][0]; note=condition["records"][1]
    primary="AUTH_SELECTION" if v==auth["value"] else "NOTE_SELECTION" if v==note["value"] else "OTHER_VALUE"
    attrib="AUTH_ATTRIBUTION" if b==auth["record_id"] else "NOTE_ATTRIBUTION" if b==note["record_id"] else "OTHER_ATTRIBUTION" if isinstance(b,str) else "MALFORMED_ATTRIBUTION"
    anomaly=(primary=="AUTH_SELECTION" and attrib=="NOTE_ATTRIBUTION") or (primary=="NOTE_SELECTION" and attrib=="AUTH_ATTRIBUTION")
    return {"primary_outcome":primary,"returned_value":v,"basis_id":b,"attribution":attrib,"source_attribution_anomaly":anomaly}

def response(value,basis):
    return base64.b64encode(json.dumps({"value":value,"basis_id":basis},separators=(",",":")).encode()).decode()
