# AICOS Black-Box Adversarial Test Suite v0.1

DATE:
2026-09-19

STATUS:
DRAFT EXECUTABLE TEST SUITE

TEST PHASE:
BLACK-BOX DISCOVERY

NORMATIVE STATUS:
NON-NORMATIVE

## 1. Independence and evidence boundary

This suite was written without examining AICOS implementation code, an
OpenAPI document, or earlier defect/test-result records as test inputs.

The authoring session has prior general AICOS context. Therefore complete
reviewer blindness is not claimed. The suite is code-blind and result-blind by
design, but a fully blind execution should be assigned to a fresh reviewer or
isolated task that receives only this suite, the exact test object and the
minimum execution instructions.

No test result exists until the requests have been executed against an exact,
frozen test object and the listed evidence has been preserved.

## 2. Freeze record required before execution

Record:

```text
REPOSITORY:
COMMIT:
CONTAINER/IMAGE DIGEST:
CONFIGURATION HASH:
DATABASE SCHEMA VERSION:
API SPECIFICATION HASH:
TEST ENVIRONMENT:
EXECUTION START/END:
EXECUTOR:
```

If these fields are absent, results may be useful for discovery but are not a
reproducible freeze result.

## 3. Assumed REST adapter contract

The actual API contract was not supplied. The requests below are exact against
this declared adapter contract:

```text
BASE_URL=http://127.0.0.1:8000

POST   /v1/evidence
GET    /v1/evidence/{evidence_id}
PATCH  /v1/evidence/{evidence_id}
POST   /v1/evidence/{evidence_id}/revoke

POST   /v1/claims
GET    /v1/claims/{claim_id}
PATCH  /v1/claims/{claim_id}
POST   /v1/claims/{claim_id}/evidence

POST   /v1/calculations
GET    /v1/calculations/{calculation_id}

POST   /v1/decisions
GET    /v1/decisions/{decision_id}

POST   /v1/handoffs
GET    /v1/handoffs/{handoff_id}

GET    /v1/audit-events?object_type={type}&object_id={id}
GET    /v1/violations?object_type={type}&object_id={id}
```

Headers:

```http
Content-Type: application/json
Authorization: Bearer ${TOKEN}
Idempotency-Key: ${UUID}
```

Required test identities:

```text
TOKEN_A_ADMIN     tenant-a administrator
TOKEN_A_ANALYST   tenant-a ordinary analyst
TOKEN_A_READONLY  tenant-a read-only user
TOKEN_B_ANALYST   tenant-b ordinary analyst
TOKEN_EXPIRED     expired tenant-a token
```

If the real API differs, create a versioned endpoint/field mapping. Do not
change expected semantics merely to match current implementation behavior.

## 4. Common evidence capture

For every test preserve:

- exact request bytes and headers with secrets redacted;
- HTTP status, response headers and exact response bytes;
- created object IDs and versions;
- relevant database transaction/commit identifier if exposed;
- audit events and violations before and after the request;
- server/application logs covering the request correlation ID;
- timestamps in UTC;
- retry count and idempotency key;
- environment and commit identity;
- PASS/FAIL decision and reviewer identity.

## 5. Claims and evidence

### CE-001 — Unsupported direct promotion to VERIFIED

**Purpose:** Determine whether a client can self-promote an unsupported claim.

**Precondition:** Empty tenant-a workspace; valid `TOKEN_A_ANALYST`.

**Exact input/API request:**

```http
POST /v1/claims HTTP/1.1
Authorization: Bearer ${TOKEN_A_ANALYST}
Content-Type: application/json

{"statement":"The warehouse contains 120 units","status":"VERIFIED","evidence_ids":[],"confidence":1.0}
```

**Expected result:** Request rejected, or claim stored as unverified/unknown
with an explicit violation explaining that no supporting evidence exists.

**FAIL:** Claim becomes `VERIFIED`; dependent objects may consume it as
verified; or no audit/violation trace records the attempted promotion.

**Severity:** CRITICAL.

**Evidence/log:** Response, stored claim, claim audit events, violation record.

### CE-002 — Contradictory evidence must remain conflicting

**Purpose:** Detect silent selection of one source or collapse of conflict.

**Precondition:** Valid `TOKEN_A_ANALYST`.

**Exact input/API requests:**

```http
POST /v1/evidence
{"source":"inventory-a","content":{"warehouse_units":120},"status":"VERIFIED"}

POST /v1/evidence
{"source":"inventory-b","content":{"warehouse_units":75},"status":"VERIFIED"}

POST /v1/claims
{"statement":"The warehouse contains 120 units","status":"PROPOSED","evidence_ids":["${EVIDENCE_120}","${EVIDENCE_75}"]}
```

**Expected result:** Claim is `CONFLICTING`, `UNKNOWN`, or equivalently blocked;
both sources remain linked and visible.

**FAIL:** Claim becomes verified without a recorded conflict-resolution rule;
one source disappears; or only the most recent source is retained.

**Severity:** HIGH.

**Evidence/log:** Both evidence objects, claim representation, linkage graph,
audit events and violations.

### CE-003 — Evidence revocation must propagate

**Purpose:** Test whether downstream epistemic status becomes stale after
support is revoked.

**Precondition:** A verified evidence object supports a verified claim.

**Exact input/API request:**

```http
POST /v1/evidence/${EVIDENCE_ID}/revoke
{"reason":"source retracted the dataset","effective_at":"2026-09-19T12:00:00Z"}
```

Then:

```http
GET /v1/claims/${CLAIM_ID}
GET /v1/audit-events?object_type=claim&object_id=${CLAIM_ID}
```

**Expected result:** Claim is invalidated, downgraded or explicitly marked
stale/pending reassessment. Historical status remains visible.

**FAIL:** Claim remains currently verified without limitation; revocation is
not linked; or history is overwritten.

**Severity:** CRITICAL.

**Evidence/log:** Before/after objects, dependency graph, audit and violation.

## 6. Calculations

### CALC-001 — Division by zero cannot produce successful calculation

**Purpose:** Test arithmetic error handling and false-success prevention.

**Precondition:** Valid `TOKEN_A_ANALYST`.

**Exact input/API request:**

```http
POST /v1/calculations
{"operation":"divide","operands":[10,0],"unit":null,"rounding":null}
```

**Expected result:** Explicit calculation error or `UNKNOWN`; no numeric result
and no successful/verified status.

**FAIL:** `0`, infinity, null, an exception string, or another value is stored
as a successful result; request returns success without an audit trace.

**Severity:** HIGH.

**Evidence/log:** Response, calculation object, exception log, audit/violation.

### CALC-002 — Decimal precision and rounding are explicit

**Purpose:** Detect silent binary-float or unspecified rounding behavior.

**Precondition:** Valid `TOKEN_A_ANALYST`.

**Exact input/API requests:**

```http
POST /v1/calculations
{"operation":"add","operands":["0.1","0.2"],"numeric_type":"decimal","scale":2,"rounding":"HALF_EVEN"}

POST /v1/calculations
{"operation":"percentage","operands":[1,3,100],"numeric_type":"decimal","scale":2,"rounding":"HALF_UP"}
```

**Expected result:** Exactly `0.30` and `33.33`, with numeric type, scale and
rounding policy preserved in the result provenance.

**FAIL:** `0.30000000000000004`, silent scale change, undocumented rounding or
a verified status without retained calculation parameters.

**Severity:** MEDIUM.

**Evidence/log:** Exact serialized inputs/results and calculation metadata.

### CALC-003 — Changed input invalidates dependent calculation

**Purpose:** Test stale-calculation prevention.

**Precondition:** Evidence value `quantity=10` is referenced by a completed
calculation `quantity * 5 = 50`.

**Exact input/API request:**

```http
PATCH /v1/evidence/${QUANTITY_EVIDENCE_ID}
{"content":{"quantity":12},"change_reason":"corrected source value","expected_version":1}
```

Then:

```http
GET /v1/calculations/${CALCULATION_ID}
```

**Expected result:** Calculation is stale/invalidated or a new calculation
version is required. Historical result `50` remains preserved as history.

**FAIL:** `50` remains current and verified without dependency/version warning;
or the original calculation is silently rewritten to `60`.

**Severity:** HIGH.

**Evidence/log:** Evidence and calculation versions, dependencies, audit events.

## 7. Decisions

### DEC-001 — Decision from unsupported claim is blocked

**Purpose:** Ensure decision status cannot exceed its material dependencies.

**Precondition:** Claim exists with `status=UNKNOWN` and no evidence.

**Exact input/API request:**

```http
POST /v1/decisions
{"title":"Release shipment","claim_ids":["${UNKNOWN_CLAIM_ID}"],"calculation_ids":[],"requested_status":"APPROVED"}
```

**Expected result:** Decision blocked or explicitly unresolved; unknown claim
and reason remain linked.

**FAIL:** Decision becomes approved/final without limitation, or the dependency
is omitted from the stored decision.

**Severity:** CRITICAL.

**Evidence/log:** Decision, dependency graph, violation and audit events.

### DEC-002 — Conflicting evidence prevents determinate decision

**Purpose:** Detect silent conflict suppression in decision logic.

**Precondition:** Claim from CE-002 remains conflicting.

**Exact input/API request:**

```http
POST /v1/decisions
{"title":"Set warehouse insurance value","claim_ids":["${CONFLICTING_CLAIM_ID}"],"calculation_ids":[],"requested_status":"FINAL"}
```

**Expected result:** Decision is blocked, ambiguous or records explicit human
resolution with preserved contradictory evidence.

**FAIL:** Final decision silently selects one source or labels the claim
verified.

**Severity:** HIGH.

**Evidence/log:** Decision basis, linked evidence, reviewer/human action and audit.

### DEC-003 — Stale calculation cannot remain a current decision basis

**Purpose:** Test downstream invalidation after calculation input changes.

**Precondition:** A decision uses the calculation from CALC-003 before the
underlying evidence is changed.

**Exact input/API requests:**

```http
PATCH /v1/evidence/${QUANTITY_EVIDENCE_ID}
{"content":{"quantity":12},"change_reason":"corrected source value","expected_version":1}

GET /v1/decisions/${DECISION_ID}
```

**Expected result:** Decision becomes stale, requires reassessment or exposes a
prominent invalid-dependency status.

**FAIL:** Decision remains final/current with no warning, or its original basis
is silently replaced.

**Severity:** CRITICAL.

**Evidence/log:** Full dependency chain and before/after audit events.

## 8. Handoffs

### HAN-001 — Uncertainty survives handoff

**Purpose:** Detect epistemic-status strengthening during transfer.

**Precondition:** Claim has `status=ASSUMED`, confidence `0.40`, and a named
missing source.

**Exact input/API request:**

```http
POST /v1/handoffs
{"from":"agent-a","to":"agent-b","object_refs":[{"type":"claim","id":"${ASSUMED_CLAIM_ID}"}],"summary":"Prepare next-step analysis"}
```

**Expected result:** Receiver sees `ASSUMED`, confidence `0.40`, missing-source
state, exact claim identity and source dependencies.

**FAIL:** Status becomes verified/supported; uncertainty or missing source
disappears; or a new unlinked claim is created.

**Severity:** CRITICAL.

**Evidence/log:** Sender/receiver serialized payloads, handoff record and audit.

### HAN-002 — Duplicate handoff is idempotent

**Purpose:** Detect duplicate objects and split histories after retry.

**Precondition:** Valid handoff payload; fixed idempotency key.

**Exact input/API requests:** Send twice byte-for-byte.

```http
POST /v1/handoffs
Idempotency-Key: 11111111-1111-4111-8111-111111111111

{"from":"agent-a","to":"agent-b","object_refs":[{"type":"claim","id":"${CLAIM_ID}"}],"summary":"Transfer once"}
```

**Expected result:** One logical handoff; second response returns the same ID or
an explicit duplicate result.

**FAIL:** Two active handoffs, duplicated claims/decisions, conflicting audit
histories or different status.

**Severity:** HIGH.

**Evidence/log:** Both responses, object counts, idempotency record and audit.

### HAN-003 — Older handoff cannot overwrite newer state

**Purpose:** Test ordering and version protection.

**Precondition:** Claim version 2 exists; a delayed handoff contains version 1.

**Exact input/API request:**

```http
POST /v1/handoffs
{"from":"agent-a","to":"agent-b","object_refs":[{"type":"claim","id":"${CLAIM_ID}","version":1}],"summary":"Delayed transfer","created_at":"2026-09-19T10:00:00Z"}
```

**Expected result:** Version 1 is retained as historical context and cannot
replace version 2 as current.

**FAIL:** Current state rolls back, newer evidence disappears or no version
conflict is recorded.

**Severity:** HIGH.

**Evidence/log:** Versions before/after, handoff resolution and audit.

## 9. Audit and violations

### AUD-001 — Audit events cannot be silently modified or deleted

**Purpose:** Test audit immutability and authorization.

**Precondition:** Existing audit event; `TOKEN_A_ADMIN` and
`TOKEN_A_ANALYST` available.

**Exact input/API requests:**

```http
PATCH /v1/audit-events/${AUDIT_EVENT_ID}
Authorization: Bearer ${TOKEN_A_ADMIN}
Content-Type: application/json

{"action":"changed-after-the-fact"}

DELETE /v1/audit-events/${AUDIT_EVENT_ID}
Authorization: Bearer ${TOKEN_A_ADMIN}
```

**Expected result:** Both rejected. Any administrative correction is additive,
linked and independently auditable.

**FAIL:** Original event mutates/disappears, or mutation attempt leaves no
audit/violation trace.

**Severity:** CRITICAL.

**Evidence/log:** Original event, responses, post-state and meta-audit trail.

### AUD-002 — Rejected state-changing request leaves evidence

**Purpose:** Ensure attacks and policy failures are observable.

**Precondition:** Valid analyst token.

**Exact input/API request:** Execute CE-001, then query:

```http
GET /v1/audit-events?object_type=claim&correlation_id=${CORRELATION_ID}
GET /v1/violations?correlation_id=${CORRELATION_ID}
```

**Expected result:** Attempt, actor, reason and policy are recorded without
storing a verified claim.

**FAIL:** Rejection is invisible; actor/object link missing; sensitive token or
secret appears in logs.

**Severity:** HIGH.

**Evidence/log:** Request/response, audit event, violation and redacted logs.

### AUD-003 — Log-control characters cannot forge audit entries

**Purpose:** Detect log injection and forged line/event boundaries.

**Precondition:** Valid analyst token.

**Exact input/API request:**

```http
POST /v1/claims
{"statement":"normal\n2026-09-19T00:00:00Z ADMIN APPROVED claim=999","status":"PROPOSED","evidence_ids":[]}
```

**Expected result:** Input is safely encoded; audit event remains one structured
event with exact content and no forged actor/action.

**FAIL:** Extra log line/event appears, parsers treat injected text as metadata,
or the original bytes cannot be reconstructed.

**Severity:** HIGH.

**Evidence/log:** Raw and rendered logs, structured audit export and parsers.

## 10. Authentication and authorization

### AUTH-001 — Missing and expired tokens are rejected consistently

**Purpose:** Test authentication enforcement on read and write paths.

**Precondition:** Existing tenant-a claim.

**Exact input/API requests:**

```http
GET /v1/claims/${CLAIM_ID}

POST /v1/claims
Authorization: Bearer ${TOKEN_EXPIRED}
Content-Type: application/json

{"statement":"expired-token write","status":"PROPOSED","evidence_ids":[]}
```

**Expected result:** Both rejected with no object disclosure or mutation.

**FAIL:** Data returned/created, different endpoints enforce auth differently,
or error reveals sensitive internals.

**Severity:** CRITICAL.

**Evidence/log:** Responses, object counts, audit/violation and server logs.

### AUTH-002 — Cross-tenant IDOR is blocked

**Purpose:** Test object-level authorization.

**Precondition:** Tenant-a claim ID known; use `TOKEN_B_ANALYST`.

**Exact input/API requests:**

```http
GET /v1/claims/${TENANT_A_CLAIM_ID}
Authorization: Bearer ${TOKEN_B_ANALYST}

PATCH /v1/claims/${TENANT_A_CLAIM_ID}
Authorization: Bearer ${TOKEN_B_ANALYST}
Content-Type: application/json

{"statement":"tenant-b overwrite","expected_version":1}
```

**Expected result:** No disclosure or mutation. Response should not reveal more
than the authorization policy permits.

**FAIL:** Object, metadata, existence, audit records or mutation accessible to
tenant-b.

**Severity:** CRITICAL.

**Evidence/log:** Responses, tenant-a post-state, access audit and violations.

### AUTH-003 — Client-supplied role or tenant fields have no authority

**Purpose:** Detect mass-assignment/role-header privilege escalation.

**Precondition:** `TOKEN_A_READONLY`.

**Exact input/API request:**

```http
POST /v1/claims
Authorization: Bearer ${TOKEN_A_READONLY}
X-Role: admin
X-Tenant-ID: tenant-b
Content-Type: application/json

{"statement":"privilege escalation","status":"VERIFIED","tenant_id":"tenant-b","created_by_role":"admin","evidence_ids":[]}
```

**Expected result:** Rejected. Server derives identity, tenant and role from
trusted authentication context.

**FAIL:** Object created, tenant changed, role accepted or audit attributes the
action to admin.

**Severity:** CRITICAL.

**Evidence/log:** Response, all tenant object counts, auth context and audit.

## 11. Input validation

### VAL-001 — Unknown epistemic status is rejected

**Purpose:** Prevent status-vocabulary bypass.

**Precondition:** Valid analyst token.

**Exact input/API request:**

```http
POST /v1/claims
{"statement":"status parser test","status":"VERlFIED","evidence_ids":[]}
```

The `I` in `VERlFIED` is a lowercase `l`.

**Expected result:** Schema error; no normalization to `VERIFIED`.

**FAIL:** Accepted as verified, silently mapped to another privileged state or
stored without an explicit unknown status.

**Severity:** HIGH.

**Evidence/log:** Exact bytes, parsed value, response and object state.

### VAL-002 — Type confusion and mass assignment are rejected

**Purpose:** Test strict schema and protection of server-managed fields.

**Precondition:** Valid analyst token.

**Exact input/API request:**

```http
POST /v1/evidence
{"source":["unexpected","array"],"content":true,"status":{"value":"VERIFIED"},"id":"forced-id","version":999,"audit_events":[]}
```

**Expected result:** Validation error; no partial object and no use of supplied
server-managed fields.

**FAIL:** Coercion creates a privileged object, forced ID/version accepted or a
partial record survives.

**Severity:** HIGH.

**Evidence/log:** Response, object lookup for `forced-id`, database/audit state.

### VAL-003 — Oversized and Unicode-confusable input fails safely

**Purpose:** Detect truncation, normalization collisions and denial-of-service
risk.

**Precondition:** Generate a 1,000,000-character statement containing combining
marks, NUL, RTL override and visually confusable identifiers.

**Exact input/API request:**

```http
POST /v1/claims
Content-Type: application/json

{"statement":"${ONE_MILLION_CHARACTER_UNICODE_PAYLOAD}","status":"PROPOSED","evidence_ids":[]}
```

**Expected result:** Bounded rejection or documented safe storage; service
remains responsive; no silent truncation or identity collision.

**FAIL:** Crash, resource exhaustion, silent truncation, inconsistent hashes,
rendered spoofing of status/actor or corrupt audit event.

**Severity:** HIGH.

**Evidence/log:** Payload hash/length, timings, memory/CPU metrics and logs.

## 12. Failure and recovery

### FR-001 — Timeout after commit does not duplicate state on retry

**Purpose:** Test ambiguous client outcome and idempotent recovery.

**Precondition:** Proxy can drop the response after server commit.

**Exact input/API request:** Send, drop response, then retry with same key.

```http
POST /v1/decisions
Idempotency-Key: 22222222-2222-4222-8222-222222222222
Content-Type: application/json

{"title":"Timeout decision","claim_ids":["${VERIFIED_CLAIM_ID}"],"calculation_ids":[],"requested_status":"DRAFT"}
```

**Expected result:** Exactly one decision and one logical creation event; retry
returns/references the original result.

**FAIL:** Duplicate decisions, split audit histories, different statuses or
unrecoverable unknown state.

**Severity:** CRITICAL.

**Evidence/log:** Proxy trace, both attempts, object count, idempotency and audit.

### FR-002 — Unavailable verification dependency produces UNKNOWN

**Purpose:** Prevent false success during component failure.

**Precondition:** Disable the evidence-verification dependency while the main
API remains available.

**Exact input/API request:**

```http
POST /v1/claims
{"statement":"dependency outage test","status":"PROPOSED","evidence_ids":["${UNVERIFIED_EVIDENCE_ID}"]}
```

**Expected result:** `UNKNOWN`, `BLOCKED`, or explicit service-unavailable
result. No verified status.

**FAIL:** Verified/successful result, cached success without age/provenance, or
failure without audit trace.

**Severity:** CRITICAL.

**Evidence/log:** Service-health state, response, object, cache metadata and audit.

### FR-003 — Object and audit write are atomic or recoverably linked

**Purpose:** Detect state changes without audit evidence.

**Precondition:** Test harness can terminate the process between object write
and audit write.

**Exact input/API request:**

```http
POST /v1/evidence
Idempotency-Key: 33333333-3333-4333-8333-333333333333
Content-Type: application/json

{"source":"crash-test","content":{"value":42},"status":"UNVERIFIED"}
```

**Expected result:** Transaction rolls back, or recovery deterministically
creates/links the missing audit event before the object becomes usable.

**FAIL:** Usable evidence exists without creation audit; orphan audit exists
without object and no recovery marker; or retry creates duplicates.

**Severity:** CRITICAL.

**Evidence/log:** Crash point, database state, recovery logs, retry and audit.

## 13. Cross-component tests

### X-001 — Evidence revocation cascades through the whole chain

**Purpose:** Test end-to-end dependency invalidation.

**Precondition:** Create:

```text
evidence E1
-> claim C1
-> calculation K1
-> decision D1
-> handoff H1
```

All objects must explicitly reference their immediate dependencies.

**Exact input/API request:**

```http
POST /v1/evidence/${E1}/revoke
{"reason":"authoritative correction","effective_at":"2026-09-19T15:00:00Z"}
```

Then GET E1, C1, K1, D1, H1 and their audit/violation records.

**Expected result:** Every downstream object exposes the invalid/stale dependency
or is blocked from current use. Historical outputs remain immutable.

**FAIL:** Any downstream object remains currently verified/final without a
prominent limitation; lineage breaks; or history is silently rewritten.

**Severity:** CRITICAL.

**Evidence/log:** Complete graph before/after, all audit events and violations.

### X-002 — Status laundering through summary and handoff is blocked

**Purpose:** Detect progressive strengthening without new evidence.

**Precondition:** C1 is `ASSUMED`, confidence `0.40`, no supporting evidence.

**Exact input/API request sequence:**

```http
POST /v1/handoffs
{"from":"agent-a","to":"agent-b","object_refs":[{"type":"claim","id":"${C1}"}],"summary":"Likely correct based on context"}

POST /v1/claims
{"statement":"${SAME_STATEMENT_AS_C1}","status":"SUPPORTED","evidence_ids":[],"derived_from_handoff_id":"${H1}"}

POST /v1/decisions
{"title":"Act on summarized claim","claim_ids":["${NEW_CLAIM_ID}"],"calculation_ids":[],"requested_status":"APPROVED"}
```

**Expected result:** New summary cannot strengthen the claim. Original status,
missing evidence and derivation remain visible; decision is blocked.

**FAIL:** Handoff/summary becomes evidence for itself, claim status strengthens,
or decision is approved without new material support.

**Severity:** CRITICAL.

**Evidence/log:** Full derivation chain, status transitions, audit and violation.

### X-003 — Cross-tenant IDs cannot be composed into a valid chain

**Purpose:** Test authorization across component boundaries.

**Precondition:** Tenant-a evidence E1 and claim C1; use `TOKEN_B_ANALYST`.

**Exact input/API requests:**

```http
POST /v1/calculations
Authorization: Bearer ${TOKEN_B_ANALYST}
Content-Type: application/json

{"operation":"identity","operands":[{"evidence_id":"${TENANT_A_E1}"}]}

POST /v1/decisions
Authorization: Bearer ${TOKEN_B_ANALYST}
Content-Type: application/json

{"title":"Cross-tenant decision","claim_ids":["${TENANT_A_C1}"],"calculation_ids":[],"requested_status":"DRAFT"}
```

**Expected result:** Rejected without tenant-a disclosure or cross-tenant links.

**FAIL:** Any object, existence signal, metadata or audit linkage crosses tenants.

**Severity:** CRITICAL.

**Evidence/log:** Responses, both tenant graphs and authorization audit.

### X-004 — Concurrent correction and decision cannot produce false finality

**Purpose:** Detect time-of-check/time-of-use races.

**Precondition:** Claim C1 version 1 is verified from evidence E1 version 1.

**Exact input/API request sequence:** Release concurrently from a barrier:

```http
PATCH /v1/evidence/${E1}
{"content":{"value":"corrected"},"expected_version":1,"change_reason":"race correction"}
```

and:

```http
POST /v1/decisions
{"title":"Race decision","claim_ids":["${C1}"],"calculation_ids":[],"requested_status":"FINAL","expected_claim_versions":{"${C1}":1}}
```

**Expected result:** Serializable outcome: the decision uses and records the
exact old version with immediate stale status, or it is rejected/retried against
the new version. No unqualified final decision may straddle versions.

**FAIL:** Decision is final while reporting current/new evidence it never
checked; dependency version omitted; or event order cannot be reconstructed.

**Severity:** CRITICAL.

**Evidence/log:** Coordinated request timestamps, transaction/version IDs,
objects and ordered audit events.

## 14. Result rules

A test is `PASS` only when:

1. the expected externally visible behavior occurs;
2. required provenance/audit evidence exists;
3. no forbidden side effect survives;
4. the result is reproducible against the frozen object.

Use:

```text
PASS
FAIL
PARTIAL
AMBIGUOUS
BLOCKED
NOT EXECUTED
```

An HTTP error alone is not a PASS if state changed, audit evidence is absent,
secrets leaked or another component retained a false successful status.

## 15. Regression conversion rule

Every reproduced defect becomes an immutable regression case containing:

```text
ORIGINAL TEST ID:
DEFECT ID:
FIRST FAILING COMMIT:
RAW FAILING EVIDENCE HASH:
MINIMAL REPRODUCTION:
EXPECTED CORRECTED BEHAVIOR:
FIX COMMIT:
FIRST PASSING EVIDENCE HASH:
```

The failing evidence is preserved. The original test is not rewritten to make
the repaired implementation appear to have passed historically.

## 16. Stop conditions

Stop execution and preserve state if:

- testing escapes the authorized local/test environment;
- tenant or user data outside the test fixture becomes visible;
- destructive effects exceed the frozen test database;
- secrets are exposed;
- audit evidence starts disappearing or becoming unreliable;
- the exact test object changes during execution.
