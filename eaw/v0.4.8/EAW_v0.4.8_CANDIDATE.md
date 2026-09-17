# NL-001 External Activity Witness
## Abstract Contract v0.4.8 — CANDIDATE

### Status

```text
CANDIDATE
NOT YET FROZEN
IMPLEMENTATION: NONE

CURRENT CANDIDATE STATUS (v0.4.8):
F-2: PATCHED / CLOSURE NOT VERIFIED (second patch round for this finding; the v0.4.7 patch was found insufficient by independent adversarial review — see change record)
F-6: OPEN — CONTENT NOT PROVIDED, NOT PATCHED
F-7: OPEN — CONTENT NOT PROVIDED, NOT PATCHED
F-8: OPEN — CONTENT NOT PROVIDED, NOT PATCHED

PRIOR PATCH ROUNDS (v0.4.4–v0.4.7; carried as record, not re-verified in this file):
F-2 (v0.4.7 patch): superseded by the v0.4.8 patch to the same finding, see change record
F-1, F-3, F-4, F-5: patched in v0.4.6, closure not verified
N1, N2, N4, N5, N6: patched in v0.4.5, closure not verified
N3: not patched in v0.4.5, documented known overblocking
D1, D2, D3, D4: patched in v0.4.4, closure not verified
D5: superseded by v0.4.5 §18 role definition (N4)

HISTORICAL REVIEW STATUS (as reported by earlier, separate closure-review documents; informational only, not re-verified in this file, not current closure for this candidate version):
Finding 1 (v0.4.2 adversarial review): reported PARTIALLY CLOSED, residual noted
Finding 2 (v0.4.2 adversarial review): reported CLOSED against named counterexamples by a same-author closure review
Finding 3 (v0.4.2 adversarial review): reported CLOSED against named counterexamples by a same-author closure review
```

Fyndstatus ovan är integrationsstatus. En separat closure-granskning måste identifiera den exakta kontraktsversion och de motexempel som granskats innan någon senare statusändring görs.

Detta dokument definierar endast ett **logiskt och epistemiskt giltighetskontrakt**.

Det etablerar **inte** att någon implementation för närvarande uppfyller kontraktet.

Det etablerar inte universell observation, sanningen i evidence-innehåll eller korrektheten hos det underliggande systemet.

NL-001 v0.7 innehåller inte denna mekanism enligt den tidigare separata v0.7-granskningen. External Activity Witness är ett föreslaget nytt tillitslager / arkitekturtillägg.

Blocker 4 i NL-001 v0.7 förblir därför öppen.

---

# 1. Kärnseparation

Modellen skiljer mellan tre saker:

```text
COVERAGE_CLAIM
      ↓
EVIDENCE_BASIS
      ↓
COVERAGE_ASSESSMENT
```

### COVERAGE_CLAIM

Ett påstående från en observer om coverage för ett specificerat intervall och scope.

En coverage-claim är inte självvaliderande.

### EVIDENCE_BASIS

Det exakta konkreta material som används när claimen bedöms.

### COVERAGE_ASSESSMENT

Beslutssystemets slutsats efter att claimen och dess evidence basis har bedömts mot detta kontrakt.

Claim, evidence och assessment får inte behandlas som utbytbara.

---

# 2. Coverage-claimens identitet

En coverage-claim måste vara bunden till minst:

```text
claim_id
observer_instance
observation_epoch
storage_instance
coverage_scope
covered_interval
event_history_reference
contract_version
threat_model_version
```

Dessa fält identifierar vad som påstås.

Deras existens bevisar inte claimen.

Coverage gäller endast inom det scope, intervall, de instanser, den kontraktsversion och den hotmodell som assessmentet avser.

---

# 3. Exakt evidence basis är obligatoriskt

Varje assessment måste vara entydigt bundet till exakt det underlag som användes för att producera det.

Konceptuellt:

```text
assessment_id
claim_id

evidence_basis:
    observer_evidence_identity
    event_history_identity
    state_binding_identity
    ordering_evidence_identity
    finality_evidence_identity

contract_version
threat_model_version
prerequisite_contract_identity
assessment_scope
assessment_interval

decision
decision_time
```

Evidence-identiteten måste förhindra att senare förändrat material tyst behandlas som samma evidence basis.

En kryptografisk digest är en möjlig mekanism.

En hänvisning till muterbart innehåll är inte ensam tillräcklig.

Varje assessment ska identifiera den normativa contract definition som används för bedömningen — vilka paragrafer i detta kontrakt, vid den angivna `contract_version`, som styr claimen. Om assessmentet därutöver är bundet till ett claim-specifikt prerequisite contract enligt §9.0 ska evidence basis separat identifiera detta genom `prerequisite_contract_identity`. En semantisk bindning till ett prerequisite contract utan denna identitet är inte en fullständig evidence-identitet enligt denna paragraf.

Ett senare reassessment använder en ny assessment-identitet och ett nytt entydigt identifierat evidence basis.

---

# 4. Coverage finality har två separata krav

Coverage genom gräns `B` kräver både:

```text
OBSERVATION_FINALITY
AND
HISTORY_FINALITY
```

## 4.1 Observation finality

Det finns giltigt stöd för att observationen för intervallet genom `B`, enligt observationsmekanismens definierade garantier, är avslutad.

Det innebär att en relevant förändring som inträffade före `B` inte fortfarande kan vara möjlig att upptäcka senare enligt mekanismens egen garanti.

Observation finality får inte härledas enbart från att inget event för närvarande väntar.

## 4.2 History finality

Det finns giltigt stöd för att alla events som observationsmekanismen kräver för det slutna intervallet genom `B` finns i den bevarade eventhistorik som detta assessment faktiskt använder.

Det omfattar events som tidigare kan ha varit:

- upptäckta men köade;
- genererade men ännu inte levererade;
- levererade men ännu inte durable/bevarade.

Observation finality och history finality är olika egenskaper.

---

# 5. Tom pipeline etablerar inte fullständighet

Exempel:

```text
queue_empty = true
```

etablerar inte:

```text
observation_complete = true
```

och etablerar inte:

```text
history_complete = true
```

En relevant förändring kan ha inträffat men ännu inte upptäckts eller omvandlats till ett event.

Finality måste därför komma från observationsmekanismens definierade garantier och evidence, inte enbart från frånvaro av väntande arbete.

---

# 6. Coverage validity requirements

För att en coverage-claim ska kunna accepteras måste evidence basis för just detta assessment stödja samtliga obligatoriska villkor som är relevanta för claimen.

### NON_SELF_ASSERTION_VALIDITY — obligatoriskt acceptansvillkor

För varje säkerhetsrelevant egenskap som krävs för godkännande ska assessmentet identifiera egenskapen, det konkreta underlag som stöder just den egenskapen, relevanta felaktiga förlopp inom den frysta hotmodellen samt varför underlaget och deklarerade tillitsantaganden bär slutsatsen mot dessa förlopp.

Att skilja ett giltigt förlopp från ett enskilt motförlopp är inte ensamt tillräckligt för godkännande.

Varje säkerhetsrelevant egenskap som är nödvändig för ett ACCEPTED-resultat omfattas av property-relevant non-self-assertion. Detta inkluderar även påståenden om kontrolldomänsoberoende och history integrity. En sådan egenskap får inte godtas enbart genom påståenden från den bedömda komponenten eller från en part vars kontrolldomän inte är oberoende styrkt. Stödet för den relevanta säkerhetsslutsatsen måste omfatta ett bevisförhållande som komponenten inte ensam kan kontrollera eller fabricera inom den frysta hotmodellen. Assessmentet ska identifiera detta förhållande och dess kontroll- och tillitsantaganden. Oberoende stöd för en annan egenskap, exempelvis avsändaridentitet, uppfyller inte detta krav. Att två instanser eller komponenter framträder som separata, har skilda namn, nycklar eller identiteter, är inte i sig tillräckligt stöd för att deras kontrolldomäner faktiskt är oberoende.

Ett påstående, en signatur eller en digest producerad under komponentens ensamma kontroll, eller under en kontrolldomän som inte är oberoende styrkt, är inte i sig tillräckligt stöd för dess egen säkerhetsrelevanta egenskap. Att en annan komponent endast bevarar eller återger samma påstående tillför inte i sig det saknade stödet, och detta gäller oavsett om den andra komponenten framträder som organisatoriskt eller tekniskt separat.

Detta villkor gäller även mekanismrelativa garantier i §§4–5 och §13, bridge-egenskaper enligt §16.1 samt tillämpliga förutsättningar enligt §9.0. Hotmodellens deklarerade antaganden får inte användas för att undanta detta obligatoriska villkor genom att likställa observerns självdeklaration med bevis för egenskapen.

Mekanismens garanti måste vara förenlig med den frysta hotmodellens erforderliga förändringsvägar och claimens prerequisite contract. Mekanismen får inte själv begränsa bort ett relevant felaktigt förlopp för att få ett godkännande.

Om obligatoriskt stöd saknas är godkännande blockerat. §7 avgör skillnaden mellan NOT_ESTABLISHED och REJECTED; kontraktet kräver ingen viss teknisk realisering av bevisförhållandet.

Den frysta hotmodellens tillitsantaganden ska vara explicit identifierade, namngivna objekt, åtskilda från evidence-established egenskaper. Assessmentet ska ange vilka säkerhetsrelevanta egenskaper som har uteslutits som icke-nödvändiga för den aktuella claimen och på vilket namngivet tillitsantagande varje sådan uteslutning vilar. Ett tillitsantagande får begränsa erforderligt scope eller erforderliga förändringsvägar enligt §17, men får inte användas — vare sig tyst eller uttryckligen deklarerat — för att undanta en egenskap som claimen, enligt sin egen definition eller tillämpliga prerequisite contract, faktiskt är beroende av. Att uteslutningen görs öppet i stället för tyst ändrar inte detta.

Ett påstående om kontrolldomänsoberoende mellan två parter får inte vila enbart på ett tillitsantagande vars enda ursprung är den bedömda partens egen kontrolldomän. Detta krav gäller oavsett om tillitsantagandet är formulerat som en egenskap hos hotmodellen, en definition eller ett annat deklarerat antagande.

Ett kontrolldomänsoberoende-påstående får inte heller etableras genom stöd från en part vars eget ursprung sammanfaller (sam-origination) med de parter vars inbördes oberoende påstås. Ett sådant gemensamt ursprung upphäver stödvärdet av påståendet, oavsett hur många lager av vidareförmedling som läggs till.

Detta kontrakt kräver inte en ny oberoende part för varje tillitsantagande. Ett ACCEPTED-beslut som vilar på ett eller flera deklarerade tillitsantaganden är begränsat av dem: beslutet etablerar inte den egenskap som tillitsantagandet i stället antar, och assessmentet ska ange vilka delar av slutsatsen som vilar på evidence och vilka som vilar på deklarerad tillit. Regressen av tillitsantaganden avslutas genom deklaration enligt §17, inte genom ytterligare bevis.

### Identity validity

Evidence kan knytas till angiven observer instance och observation epoch.

Ett `observer_id`-fält bevisar inte ensamt ursprung.

### Observation-boundary validity

Observationen gäller avsedd storage instance och evidence boundary.

Återanvändning av samma logiska storage-namn får inte tyst göra en gammal och en ersatt storage-instans likvärdiga.

### Scope validity

Claimen identifierar de förändringsvägar den täcker.

Dessa förändringsvägar måste motsvara de vägar som krävs av den frysta hotmodellen för assessmentet som görs.

### Interval validity

Det täckta intervallets början och slut är entydiga.

### Ordering validity

Relationerna mellan state-bindningar, observerade events, coverage-gränser, epochövergångar och relevanta finality-punkter är etablerade.

Wall-clock timestamps behöver inte ensamma vara tillräckliga.

### Observation finality

Kravet i §4.1 är uppfyllt.

### History finality

Kravet i §4.2 är uppfyllt.

### Gap and restart validity

Failures, restarts, resets, queue loss, epoch changes eller andra avbrott får inte tyst räknas som täckta intervall.

### History integrity validity

Eventhistoriken har den integritetsnivå som den frysta hotmodellen kräver.

Kontraktet antar inte universellt manipulationssäker historik. Det skydd som påstås måste hålla sig inom de explicita tillitsantagandena.

### Evidence traceability

Assessmentet hänvisar till det exakta evidence basis som användes.

---

# 7. Coverage assessment states

En coverage-claim kan exempelvis bedömas som:

```text
ACCEPTED
NOT_ESTABLISHED
REJECTED
```

### ACCEPTED

De obligatoriska validity-villkoren har stöd för angivet scope, intervall, instanser, evidence basis, kontraktsversion och hotmodell.

### NOT_ESTABLISHED

Tillgängligt evidence är otillräckligt för att etablera de obligatoriska villkoren.

Det innebär inte att observationen definitivt misslyckades.

Det innebär att observationen för närvarande inte kan styrkas från tillgängligt evidence basis.

### REJECTED

Konkret evidence motsäger claimens giltighet enligt kontraktet.

Exempelvis kan en claim omfatta ett intervall där en observer epoch reset inträffar utan styrkt bridge.

`NOT_ESTABLISHED` och `REJECTED` får inte behandlas som likvärdiga.

---

# 8. Coverage är inte continuity

```text
COVERAGE_ACCEPTED
```

etablerar inte automatiskt något continuity-påstående om evidence-state.

Coverage betyder endast att relevanta krav på observation coverage och eventhistorik har accepterats för angivet scope och intervall.

Varje ytterligare slutsats måste bedömas separat.

---

# 9. State- och continuity-claim types

Modellen skiljer minst mellan claim types som:

```text
BOUND_AT_POINT
CURRENT_THROUGH
BYTE_CONTINUITY
OBSERVATION_CONTINUITY
```

Ingen universell styrkeordning antas mellan dessa claim types.

Specifika logiska beroenden ska vara fastställda i det prerequisite contract enligt §9.0 som används för assessmentet. Olösta förutsättningar blockerar godkännande.

## 9.0 Obligatoriska claim-specific prerequisite contracts

Varje claim type ska före granskning av underlaget ha ett entydigt identifierat och versionsbundet prerequisite contract. Assessmentet ska vara bundet till exakt denna definition och dess förutsättningar enligt §3. En implementation får inte behandla en egen, svagare definition som likvärdig med en annan definition vid jämförelse av konformitet.

Detta prerequisite contract ska ange den exakta egenskapen som påstås, evidence-scope, erforderliga förändringsvägar, punkt eller intervall, nödvändiga bindningar, coverage, finality, eventsemantik, tillitsantaganden samt regler för eventuell composition. Kraven ska vara förenliga med den frysta hotmodellen och omfattas av §6:s NON_SELF_ASSERTION_VALIDITY där den bedömda egenskapen kräver det.

Minimikrav för de namngivna typerna:

- BOUND_AT_POINT: stöd för att den identifierade bindningen motsvarar den avgränsade faktiska evidence-state som claimen avser vid den angivna punkten. Tidigare interval-coverage krävs inte generellt.
- OBSERVATION_CONTINUITY: accepterad coverage enligt §§4–7 för hela det erforderliga intervallet och scopet, med accepterad bridge enligt §16.1 vid berörda gränser. Det är slutsatsen från denna coverage och tillämplig composition, inte ett alternativ till coverage-kontrollerna. Tidigare state-binding krävs inte.
- BYTE_CONTINUITY: stöd för oförändrade evidence-bytes över hela det specificerade intervallet. Om slutsatsen härleds från observation måste underlaget styrka att alla byteförändringsvägar som påståendet kräver omfattas och att fullständig, finalized eventhistorik kan stödja just denna slutsats. Endpoint equality eller frånvaro av events i ett otillräckligt scope räcker inte.
- CURRENT_THROUGH: exakt betydelse av current för den identifierade bundna staten, den senare gränsen och det erforderliga scopet ska vara fastställd före assessmentet. Underlaget måste stödja just denna egenskap genom gränsen. BOUND_AT_POINT tillsammans med OBSERVATION_CONTINUITY är inte i sig tillräckligt om observationens scope eller eventsemantik inte bär current-påståendet. Om current avser samma exakta bytes krävs stöd som faktiskt fastställer den byteegenskap definitionen anger. Ingen universell dependency på BYTE_CONTINUITY införs.

Saknade, olösta eller otillräckligt stödda obligatoriska förutsättningar blockerar godkännande. Betydelsen av current, required scope eller andra förutsättningar får inte försvagas efter granskning för att bortförklara en oövervakad väg. Ett godkännande får inte överföras till en annan definition.

## 9.1 BOUND_AT_POINT

Frågar om en specifik evidence-state blev giltigt bunden vid en angiven punkt.

Det behöver inte nödvändigtvis kräva observation coverage över ett tidigare intervall.

## 9.2 CURRENT_THROUGH

Frågar om en specificerad bunden state har tillräckligt stöd för att behandlas som current genom en senare explicit gräns.

Att en state var bunden vid `t0` etablerar inte i sig att den fortfarande är current vid `t1`.

## 9.3 BYTE_CONTINUITY

Frågar om evidence-bytes förblev oförändrade över ett specificerat intervall.

Evidence-kraven för denna claim måste faktiskt kunna stödja slutsatser om byteförändringar.

## 9.4 OBSERVATION_CONTINUITY

Frågar om giltig observation coverage är etablerad över ett specificerat intervall.

Den kräver inte att en tidigare evidence-state var bunden.

Den etablerar inte i sig byte continuity.

---

# 10. Activity-eventens semantik hålls medvetet svag

Ett generiskt:

```text
ACTIVITY_DETECTED
```

betyder endast att relevant aktivitet, enligt observationsmekanismens definition, observerades.

Det betyder inte automatiskt:

```text
bytes_changed
attack_occurred
state_invalid
activity_explained
```

Dessa slutsatser kräver separat evidence och separata definitioner.

Ett generiskt activity-event kan blockera vissa claims utan att bevisa att evidence-bytes ändrades.

En uttryckligen observerad byte mutation kan motsäga byte continuity även när observation continuity är fullt etablerad.

---

# 11. State binding suddar inte ut tidigare osäkerhet

En senare:

```text
STATE_COMMITTED S43
```

kan etablera en ny bunden state.

Den etablerar eller reparerar inte i sig continuity över intervallet före denna bindning.

Båda kan samtidigt vara sanna:

```text
S43 = validly bound at the new point

prior interval = NOT_ESTABLISHED
```

---

# 12. Historiskt reassessment är additivt

Ett tidigare assessment kan senare omprövas om nytt interval-relevant evidence blir tillgängligt.

Exempel:

```text
Assessment A1
evidence basis E1
→ NOT_ESTABLISHED
```

Senare:

```text
Assessment A2
evidence basis E1 + E2
→ ACCEPTED
```

A1 bevaras som det historiska beslutet baserat på E1.

A2 är ett nytt assessment baserat på annat evidence.

Det tidigare beslutet skrivs inte tyst om.

En senare state commit är inte ensam evidence om ett tidigare osäkert intervall.

Ett tidigare interval-assessment får ersättas eller omprövas till en starkare slutsats endast när nytt giltigt evidence relevant för intervallet ingår. Ny assessment-id, ny digest, ny prerequisite contract, ny threat model eller ny definition är inte i sig nytt evidence.

Ett tidigare NOT_ESTABLISHED får inte bli ACCEPTED över samma redan bedömda intervall enbart genom byte av contract version, prerequisite definition, threat model eller trust assumptions.

Bevara historiskt assessment additivt.

---

# 13. Sent evidence efter accepterad finality

Anta:

```text
Assessment A17
coverage t0..t5
→ ACCEPTED
```

Senare framkommer ett relevant event som enligt observationsmekanismens egna definierade garantier borde ha ingått före finality-gränsen `t5`.

Det är inte endast en vanlig sen komplettering.

Det är evidence för att den tidigare finality-bedömningen kan ha varit ogiltig.

Det historiska A17-assessmentet bevaras som beslutet som fattades då.

Ett senare assessment måste bedöma det nya evidence och kan motsäga eller underkänna den tidigare finality-slutsatsen.

Systemet får inte fortsätta förlita sig på den tidigare accepterade finality-slutsatsen som om inget motsägande evidence hade framkommit.

---

# 14. Coverage gaps

Coverage är tidsbegränsad och positivt etablerad.

Frånvaro av ett registrerat gap-event etablerar inte obruten coverage.

Om giltigt coverage-evidence endast sträcker sig genom `t0`, och ett bortfall först upptäcks vid `t1`, börjar det ostyrkta intervallet efter den senast positivt etablerade coverage-gränsen, inte vid tidpunkten då felet upptäcktes.

```text
last established coverage = t0
failure detected = t1
```

innebär inte:

```text
coverage established through t1
```

---

# 15. Observation epochs

En `observation_epoch` identifierar en specifik observationsperiod.

En restart eller motsvarande övergång får inte tyst fortsätta föregående epoch som om inget avbrott hade inträffat.

En ny epoch etablerar inte i sig continuity med föregående epoch.

Coverage över en epoch-gräns kräver explicit stöd genom §16.1.

## 15.1 Restart / equivalent-transition assessment

Om coverage-validity eller finality beror på förekomst eller frånvaro av en restart, reset, process replacement, queue-loss transition eller annan observationsbrytande övergång ska denna egenskap bedömas separat och bindas till ett identifierat evidence basis. Bedömningen ska ange övergångsegenskapen, berört intervall, berörda instanser/epoker och slutsatsen. §3 och §6:s NON_SELF_ASSERTION_VALIDITY gäller.

Relevansen avgörs av övergångens påverkan på de observations-, leverans- och bevarandegenskaper som claimen kräver inom den frysta hotmodellen. Signalnamn, mekanismens egen benämning eller självrapporterad frånvaro av restart får inte ensamt avgöra bedömningen. En SIGTERM-relaunch med relevant köförlust får inte undantas därför att mekanismens garanti endast nämner SIGKILL.

Denna bedömningsskyldighet gäller varje faktiskt inträffad övergång inom claimens deklarerade intervall som kan bryta, förändra, förlora, undertrycka, återställa eller på annat sätt påverka den observation-, history- eller finality-linkage genom vilken evidens för claimen bevaras eller bedöms. Skyldigheten gäller oavsett om den frysta hotmodellen eller ett tillämpligt prerequisite contract enligt §9.0 klassificerar den berörda egenskapen som required för den aktuella claimen. En sådan klassificering får inte undanta skyldigheten att bedöma övergången och redovisa den evidensbasis som finns för dess förekomst och konsekvens. Om övergången blir känd först genom senare giltig evidens gäller skyldigheten från den tidpunkten och den tidigare bedömningen får endast omvärderas additivt enligt kontraktets regler för reassessment. §17 begränsar vilken slutsats bedömningen får bära, inte om denna bedömning och redovisning ska genomföras.

En bestämning om att en faktiskt inträffad övergång inom claimens deklarerade intervall inte kan bryta, förändra, förlora, undertrycka, återställa eller på annat sätt påverka den observation-, history- eller finality-linkage genom vilken evidens för claimen bevaras eller bedöms — propositionen att övergången saknade sådan påverkan — ska alltid bindas till ett identifierat evidence basis enligt §3. I den utsträckning en sådan bestämning är nödvändig för ett ACCEPTED-resultat omfattas den även av §6:s NON_SELF_ASSERTION_VALIDITY, oberoende av om §6 dessutom skulle aktiveras av andra skäl.

Frånvaro av en redovisad bestämning för en övergång som faktiskt inträffat inom claimens deklarerade intervall utgör inte i sig stöd för att övergången faller utanför §15.1:s bedömningsskyldighet, och utgör inte i sig stöd för att övergången saknade sådan påverkan. En sådan frånvaro behandlas på samma sätt som en bestämning som saknar tillräckligt stöd enligt följande mening. Finns inget sådant evidence basis, eller ger det identifierade evidence basis enligt §3 inte tillräckligt stöd för propositionen att övergången saknade sådan påverkan — inklusive, där §6 är tillämplig, dess krav — får propositionen i stället endast bäras som ett namngivet tillitsantagande enligt §17, inte som en etablerad slutsats. Ett ACCEPTED-beslut som vilar på ett sådant tillitsantagande är begränsat av det på det sätt §6:s regel för deklarerade tillitsantaganden anger och etablerar inte att övergången saknade sådan påverkan. Ett sådant tillitsantagande får inte åberopas i stället för, eller i strid med, tillgänglig evidence som faktiskt stöder eller motsäger propositionen.

En övergång bevisar inte automatiskt förlust. Men obruten coverage över den får inte godtas utan stöd för de villkor §6 anger under Observation finality, History finality, Gap and restart validity och History integrity validity för just denna övergång, och tillämplig bridge enligt §16.1. Detta stöd avgörs av dessa villkors egna definitioner, inte av om den frysta hotmodellen eller ett tillämpligt prerequisite contract enligt §9.0 klassificerar den berörda egenskapen som required. Saknat stöd eller motsägande evidence hanteras enligt §7.

---

# 16. Storage-instance identity

Coverage måste avse den faktiska storage-instans som observeras, inte endast ett återanvändbart logiskt namn.

Exempel:

```text
logical_storage = nl001-evidence
storage_instance = ST9
```

Om storage ersätts:

```text
logical_storage = nl001-evidence
storage_instance = ST10
```

får coverage för ST9 inte automatiskt appliceras på ST10.

Mekanismen genom vilken instance identity etableras är fortfarande en implementation-proof obligation.

## 16.1 BRIDGE_ASSESSMENT — composition över gränser

Ett enskilt assessment får inte självt sträcka sig över en observer-, observation-epoch- eller storage-instance-gräns. Om det underliggande intervallet eller scopet spänner över en sådan gräns ska det delas vid gränsen, och själva gränsen kräver en separat accepterad BRIDGE_ASSESSMENT enligt denna paragraf, oavsett om den spännande bedömningen framställs som ett eller flera assessments.

Coverage eller continuity över flera assessments får inte härledas genom implicit sammanslagning över observer-, observation-epoch- eller storage-instance-gränser. Varje sådan övergång som slutsatsen beror på kräver en separat accepterad BRIDGE_ASSESSMENT.

En gemensam övergripande claim i denna paragrafs mening är ett enskilt påstående — en COVERAGE_CLAIM enligt §2 eller en namngiven claim type enligt §9 — vars deklarerade scope eller intervall är avsett att härledas ur mer än ett assessments scope eller intervall tillsammans. Ett BRIDGE_ASSESSMENT som identifierar exakt två redan accepterade assessments enligt denna paragraf utgör inte i sig ytterligare en sådan övergripande claim över just de två assessmenten; kravet i detta stycke riktar sig mot den claim som skarven ska bära, inte mot bridge-assessmentets egen konstruktion.

Närhelst två eller flera separata assessments används för att stödja en gemensam övergripande claim krävs alltid en explicit accepterad BRIDGE_ASSESSMENT (även kallad COMPOSITION_ASSESSMENT) för sammanslagningen. Detta krav är ovillkorligt: det gäller oavsett om något enskilt identifierande assessment-attribut kan sägas skilja sig mellan delarna, och frågan om evidence basis-identiteten i sig räknas som ett sådant attribut är därför överflödig. Composition assessment ska identifiera de ingående delarna, skarven mellan dem, relevant scope, tillämplig claim type samt det evidence som visar att skarven bär slutsatsen, och ska uppfylla samtliga krav 1–5 nedan för just den skarven.

Den ska minst identifiera:

```text
assessment_id
left_boundary
right_boundary
left_assessment
right_assessment
bridge_claim_type
bridge_interval
bridge_scope
bridge_evidence_basis
observer/storage instances and epochs crossed
prerequisite_contract_identity
contract_version
threat_model_version
decision
decision_basis
```

Hänvisningarna ska avse exakta assessments och underlag enligt §3. Bridge-bedömningen ska uppfylla följande obligatoriska krav:

1. De ingående assessmenten är giltiga för de avsnitt och egenskaper de används för; deras scope, instanser och definitioner är förenliga med det sammansatta påståendet.
2. Gränsernas ordning, den faktiska övergången och dess intervall är styrkta. Matchande klockslag bevisar inte att övergången saknar lucka.
3. Bridge-evidence stöder just övergången, required scope och den claim type som sammanslagningen avser. Erforderlig observation, history finality, gap/restart-bedömning och historikintegritet för övergången ska vara styrkta; ett ostyrkt mellanrum får inte döljas genom sammanslagning.
4. Property-relevant non-self-assertion enligt §6 och det tillämpliga prerequisite contract enligt §9.0 är uppfyllda. En migrationsanteckning eller självdeklaration är inte ensam tillräckligt stöd.
5. Beslutet anger exakt vilken sammansatt slutsats övergången får stödja. Bridge för OBSERVATION_CONTINUITY innebär inte automatiskt bridge för BYTE_CONTINUITY eller CURRENT_THROUGH.
6. Bridge-assessmentet får inte lyfta ett ingående assessment till en starkare contract version, threat model version eller prerequisite-definition än den som det ingående assessmentet självt var ACCEPTED under. Skarvens egna `contract_version`, `threat_model_version` och `prerequisite_contract_identity` begränsar hur skarven bedöms, men ändrar inte retroaktivt vad de ingående assessmenten redan var accepterade mot.

Om stöd saknas eller motsägs får bridge inte accepteras; §7:s beslutsskillnad gäller. Två var för sig ACCEPTED assessments räcker aldrig ensamma för att etablera coverage eller continuity över en sådan gräns. Kraven gäller varje gräns i en längre kedja, även när ett ingående assessment självt bygger på tidigare composition.

Ett intervall uppdelat i n delar komponeras genom ett ändligt antal pairwise BRIDGE_ASSESSMENTs — högst n−1, ett per gräns i kedjan. Detta krav terminerar: det ändliga antal gränser som en given uppdelning faktiskt innehåller är den enda utlösaren, och denna paragraf inför inget ytterligare, rekursivt bridge-krav för de bridge-assessments som redan uppfyller kraven ovan för sin egen gräns.

---

# 17. Threat-model relativity

Coverage är aldrig universell.

Ett accepterat assessment gäller endast de förändringsvägar och tillitsantaganden som definierats av den frysta hotmodellen.

Exempelvis kan en implementation göra anspråk på skydd mot:

```text
adapter mutation
ordinary local rewrite
```

utan att göra anspråk på skydd mot:

```text
witness root compromise
physical compromise
```

Sådana gränser måste förbli explicita.

Trust elimineras inte av detta kontrakt.

Den måste deklareras.

---

# 18. Core invariants

§18 är en human-readable invariant summary och inte en komplett normativ eller maskinläsbar conformance specification. §§1–17 samt uttryckligen refererade prerequisite- och assessment-contracts enligt §9.0 och §16.1 är normativa. Där §18 sammanfattar en skyldighet som §§1–17 anger mer precist, är den mer precisa paragrafen avgörande.

## I1 — Activity invalidates assumptions of current trust where relevant

Observerad relevant aktivitet innebär att en tidigare bunden state inte automatiskt får fortsätta behandlas som current utan det ytterligare evidence som den tillämpliga claim-definitionen kräver.

## I2 — New trust requires explicit support

Att aktivitet upphör etablerar inte i sig en ny trusted state.

## I3 — Missing witness evidence is not CLEAN

Frånvaro av tillräckligt witness-evidence får inte tolkas som lyckad observation.

## I4 — Endpoint equality does not establish uninterrupted continuity

Om en state senare återgår till samma hash efter relevant aktivitet etablerar lika endpoints inte i sig obruten continuity.

## I5 — Historical trust remains distinguishable from current trust

En state kan förbli senaste giltiga historiska binding samtidigt som current status inte är etablerad.

## I6 — Witness evidence does not establish truth of contents

En giltig historisk binding bevisar inte att evidence-innehållet är sant eller korrekt.

## I7 — Coverage must be positively established

Frånvaro av ett gap-event är inte evidence för full coverage.

## I8 — Detection time does not extend coverage

Tidpunkten då ett gap upptäcks förlänger inte den senast positivt etablerade coverage-gränsen.

## I9 — Epoch transitions do not imply continuity

En ny observation epoch får inte tyst ärva continuity från föregående epoch.

## I10 — Later state commits do not repair previous interval uncertainty

En senare state binding ändrar inte i sig epistemisk status för ett tidigare intervall.

## I11 — Historical assessments may change only through relevant new evidence

Ett tidigare interval-assessment får ersättas av ett nytt assessment endast när nytt giltigt evidence relevant för intervallet ingår.

## I12 — Bound state and current state are distinct claims

Att binda en state vid en punkt etablerar inte automatiskt att den är current vid en senare gräns.

## I13 — Coverage claims are not self-validating

En claim får inte bli accepted coverage endast därför att en observer påstår den.

## I14 — Observation coverage and delivery completeness are distinct

Förmåga att observera förändringar etablerar inte att resulting event-evidence blev fullständigt bevarat.

## I15 — Coverage finality requires both observation and history finality

Ett intervall får inte behandlas som finalized förrän båda kraven är uppfyllda.

## I16 — Coverage is instance-bound

Coverage får inte tyst överföras över observer epochs eller storage-instance replacements.

## I17 — Coverage validity is threat-model-relative

Accepterad coverage gäller endast inom deklarerat scope och deklarerade antaganden.

## I18 — Continuity assessments are claim-specific

Events måste bedömas mot exakt den continuity- eller state-claim som görs.

## I19 — Finality includes latent observations

Coverage finality får inte etableras enbart därför att alla redan genererade events har levererats.

## I20 — Observation finality and history finality remain distinct

Kontraktet kräver separat stöd för båda.

## I21 — Empty pipeline does not prove completeness

Frånvaro av pending events är inte tillräckligt evidence för komplett observation eller eventhistorik.

## I22 — Assessments are evidence-set bound

Varje assessment gäller endast det exakta evidence basis, scope, intervall, instanser, kontraktsversion och hotmodellsversion som assessmentet identifierar.

## I23 — Reassessment is additive

Nytt evidence producerar ett nytt assessment. Det skriver inte retroaktivt om evidence basis eller decision context för ett tidigare assessment.

## I24 — No universal ordering between claim types

Ingen generell styrkeordning antas mellan `BYTE_CONTINUITY`, `OBSERVATION_CONTINUITY`, `CURRENT_THROUGH`, `BOUND_AT_POINT` eller framtida claim types.

Specifika beroenden kan följa av deras exakta definitioner.

## I25 — Assessment evidence identity is mandatory

Varje assessment måste entydigt identifiera exakt vilket evidence basis som bedömdes.

## I26 — Late required evidence challenges prior finality

Om evidence senare framkommer som enligt mekanismens egna garantier borde ha ingått före en tidigare accepterad finality-gräns måste den tidigare finality-slutsatsen omprövas.

Det sena evidence får inte behandlas som en vanlig post-finality komplettering.

---

# 19. Central implementation-proof obligation

Varje föreslagen implementation måste besvara:

> **Vilket konkret, entydigt identifierat evidence visar att inga relevanta förändringar inom det accepterade intervallet kan saknas ur exakt den eventhistorik som detta assessment använder, givet deklarerat scope och den frysta hotmodellens antaganden?**

Den måste dessutom separat besvara:

> **Vad skulle falsifiera implementationens påstådda observation finality?**

och:

> **Vad skulle falsifiera dess påstådda history finality?**

Om implementationen endast kan svara:

> “Observern säger att den såg allt”

har den inte uppfyllt detta kontrakt.

---

# 20. Explicit non-claims

Detta kontrakt etablerar inte:

- universell observation;
- korrekthet eller sanning i evidence-innehåll;
- frånvaro av compromise utanför den frysta hotmodellen;
- continuity enbart från lika endpoint hashes;
- coverage enbart från silence;
- current state enbart från en gammal binding;
- finality enbart därför att en queue är tom;
- trust enbart därför att metadatafält existerar.

---

# 21. Current project status

Kontraktet är:

> **NL-001 External Activity Witness — Abstract Contract v0.4.8 CANDIDATE — NOT YET FROZEN**

Status:

```text
LOGICAL / EPISTEMIC CONTRACT ONLY

IMPLEMENTATION CONFORMANCE:
NOT ESTABLISHED

EXISTING NL-001 v0.7 CAPABILITY:
NO

BLOCKER 4:
OPEN

NL-001 v0.7:
NOT_READY
REJECTED FOR WIRING
```

External Activity Witness är ett föreslaget nytt trust layer.

Ingenting i detta dokument ändrar de tidigare etablerade resultaten från den separata NL-001 v0.7-granskningen.
