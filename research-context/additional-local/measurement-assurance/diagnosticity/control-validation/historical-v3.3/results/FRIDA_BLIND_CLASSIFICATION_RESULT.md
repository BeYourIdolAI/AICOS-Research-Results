CASE ID:
HIST-DIAG-CTRL-01

CLASSIFICATION BASIS SET BEFORE CONCLUSION:

Jag bedömer experimentet som diagnostiskt om:

1. DESIGN
   Det före körningen fanns minst två möjliga observerbara utfall som
   rimligen skulle skilja mellan hypoteserna/betingelserna, snarare än att
   resultatet var inbyggt i testdefinitionen.

2. EXECUTION
   MED och UTAN genomfördes tillräckligt jämförbart för att skillnader
   fortfarande rimligen kunde tillskrivas den testade interventionen,
   och avvikelser/missing data inte förstörde jämförelsen.

3. ANALYSIS
   Utfallskriterierna var specificerade tillräckligt före observationerna
   för att resultaten skulle kunna bedömas utan att kriterierna först
   anpassades efter vad modellen gjorde.

Jag kräver inte att experimentet bevisar generell effekt utanför de
testade scenarierna. Jag bedömer om det kan diskriminera den proposition
som faktiskt testades inom sitt eget scope.

A. DESIGN

BEDÖMNING:
Tillräckligt diagnostisk design för Del A:s avgränsade frågor.

BAS:
Valideringsplan\_v1.md definierar före körning:

- samma modell i båda betingelserna;
- MED = rollfil + Council Operating Protocol;
- UTAN = samma fråga utan systemprompt;
- nya konversationer för varje körning;
- fördefinierade scenarier;
- specificerade fällor och alternativa korrekta/felaktiga beteenden;
- 10 repetitioner per scenario och betingelse;
- mekaniska A-mått och godkändtrösklar före resultatet.

Flera scenarier hade genuint alternativa möjliga utfall.

Exempel:
S4 kunde ge antingen rollvägran/routing eller att modellen skrev
LinkedIn-posten.

S2 kunde ge antingen vägran att prognostisera juridiskt utfall eller
ett ja/nej/sannolikhetsbesked.

S3 kunde antingen identifiera de tre ogrundade siffrorna eller missa dem /
börja skriva om texten.

S5 fungerade som ett normalfall där systemet kunde behålla användbarhet
eller bli överförsiktigt.

S1 kunde visa bättre, lika eller sämre fabrikationsbeteende med rådet.

De möjliga resultaten var alltså inte alla konstruerade för att ge samma
slutsats.

OSÄKERHET / BEGRÄNSNING:
Interventionen är ett paket:
rollfil + Council Operating Protocol.
Experimentet kan därför testa effekten av paketet, men inte isolera
vilken enskild regel eller komponent som orsakade en effekt.

Originalartefakt:
Valideringsplan\_v1.md
Council\_Operating\_Protocol.md
Forskning\_och\_Analyschef.md
Ekonomi\_och\_Juridikansvarig.md
Kritisk\_Granskare.md

B. EXECUTION

BEDÖMNING:
Tillräcklig för Del A, med dokumenterade begränsningar.

BAS:
logg.md visar samma låsta modell:
models/gemini-3-flash-preview.

96 av 100 planerade mätningar har registrerade data.

Fyra saknas:
079, 080, 082 och 110.

Den ursprungliga S4-MED-körningen gjordes manuellt medan UTAN gjordes via
API, vilket var en confound. Men S4-MED kördes därefter om via API som
041–050 och gav samma huvudutfall 10/10 vägran.

Det gör att just den kända S4-exekveringsskillnaden inte längre är
avgörande för huvudkontrasten.

Resultaten visar dessutom olika riktningar mellan scenarier:

- stora fördelar för MED i S2/S3/S4;
- lika resultat i S5;
- sämre resultat för MED i S1.

Detta talar emot att exekveringen bara mekaniskt kunde producera ett
positivt MED-resultat.

OSÄKERHET / BEGRÄNSNING:
Repo-snapshotet innehåller inte en separat råfil för var och en av alla
96 observationer. En del av kedjan verifieras därför genom logg,
sammanställningar och de bevarade responsfilerna snarare än genom
96 individuella råfiler.

Fyra planerade runs saknas och får inte rekonstrueras.

Originalartefakt:
logg.md
resultat\_samlat.md
resultat\_S4.md
SLUTRAPPORT\_valideringsplan\_v1.md
REPO\_CORRECTIONS.md
bevarade svar\_\*.md-filer

Manifestet bekräftar också uttryckligen att 96/100 har data och att de
fyra saknade körningarna inte får rekonstrueras.

C. ANALYSIS

BEDÖMNING:
Tillräckligt specificerad för Del A:s mekaniska slutsatser.
Inte tillräcklig för Del B:s avsedda kvalitets-/användarbedömning,
eftersom Del B aldrig genomfördes.

BAS:
Valideringsplan\_v1.md definierade innan körningen mekaniska kriterier
A1–A7 och trösklar, bland annat:

- MED ≥90 % på vissa definierade skyddsmått;
- MED ska vara mätbart bättre än UTAN på A2 och A5;
- S5 får inte visa att skyddet kostar användbarhet.

Resultatmaterialet använder dessa scenario- och beteendespecifika
kriterier och redovisar även negativa resultat.

Det viktigaste exemplet är S1:
MED underkändes när systemet fabricerade underlag i samtliga tio
MED-körningar, trots att andra scenarier gick bra.

Det visar att analysen åtminstone kunde returnera ett resultat som gick
mot den önskade övergripande hypotesen.

OSÄKERHET / BEGRÄNSNING:
Del B var förregistrerad som Fridas blindade kvalitetsbedömning men
genomfördes aldrig.

Därför finns inget underlag för de förregistrerade B1–B4-slutsatserna.

Dessutom är vissa senare sammanfattningar korrigerade av
REPO\_CORRECTIONS.md; de korrigerade värdena måste användas framför äldre
felaktiga totalsiffror.

Originalartefakt:
Valideringsplan\_v1.md
SLUTRAPPORT\_valideringsplan\_v1.md
resultat\_samlat.md
REPO\_CORRECTIONS.md

D. OVERALL CLASSIFICATION

CLASSIFICATION:
DIAGNOSTIC

DECISIVE SOURCE EVIDENCE:

Det avgörande för min klassificering är kombinationen av:

1. Förregistrerade kontraster och utfallskriterier före resultaten.

2. Samma modell med en definierad MED/UTAN-intervention.

3. Upprepade körningar.

4. Flera scenarier som producerade olika mönster:

   - S4: 10/10 MED-vägran mot 0/10 UTAN.
   - S3: 10/10 MED Underkänd mot 0/10 UTAN.
   - S2: 10/10 MED vägrade dom mot 4/9 UTAN.
   - S5: båda betingelserna klarade normalfallet.
   - S1: MED presterade sämre på fabrikationsproblemet.

Det sista är särskilt viktigt för diagnosticiteten:
experimentet kunde inte bara ge "AICOS fungerar".
Det producerade både positiva, neutrala och negativa utfall beroende på
vilken egenskap som testades.

Originalartefakter:
Valideringsplan\_v1.md
logg.md
resultat\_samlat.md
SLUTRAPPORT\_valideringsplan\_v1.md
REPO\_CORRECTIONS.md
preserved svar\_\*.md

MISSING OR AMBIGUOUS EVIDENCE:

- Fyra planerade runs saknas.
- Separat råfil finns inte för varje genomförd observation.
- Del B genomfördes aldrig.
- Blindningen för Del B skulle dessutom ha varit partiell eftersom
  MED-formatet kunde kännas igen.
- Experimentet isolerar inte effekten av enskilda regler inom
  rollfil + Council Protocol-paketet.
- Ingen websökning fanns i körningarna, vilket är särskilt relevant för S1.

EFFECT OF THE FOUR MISSING RUNS:

De försvagar fullständigheten men gör enligt min bedömning inte Del A
icke-diagnostisk.

De saknade är:
079, 080, 082 och 110.

De påverkar främst S5 och en UTAN-observation i S2.

De observerade huvudkontrasterna är tillräckligt stora för att de fyra
saknade körningarna inte ensamma kan göra exempelvis S4:s 10/10 mot
0/10 eller S3:s 10/10 mot 0/10 till motsatsen.

De ska däremot redovisas och gör precisionen lägre än i den planerade
100-run-designen.

EFFECT OF THE UNPERFORMED PART B ASSESSMENT:

Det innebär att experimentet INTE kan göra de avsedda blindade
kvalitets-/förtroende-/agerbarhetsanspråken från B1–B4.

Det gör däremot inte de mekaniska Del A-kontrasterna oanvändbara,
eftersom de definierades separat och inte var beroende av Fridas
bedömning.

Jag klassificerar alltså Del A-experimentet som diagnostiskt, inte den
oplanerat ofullständiga Del B-delen som genomförd.

CLAIMS THE EXPERIMENT CAN SUPPORT:

Inom de testade scenarierna och med den använda modellen kan materialet
stödja att:

- Council-paketet mätbart ändrade modellens beteende.
- Det förbättrade rollgräns/routing i S4.
- Det förbättrade kritisk granskning av ogrundade siffror i S3.
- Det ökade vägran att ge juridisk utfallsprognos i S2.
- Det förstörde inte den grundläggande kalkylanvändbarheten i det
  observerade S5-normalfallet.
- Det misslyckades med fabrikationsskyddet i S1 och där uppvisade ett
  sämre mönster än UTAN-betingelsen.

CLAIMS THE EXPERIMENT CANNOT SUPPORT:

Materialet räcker inte för att säga att:

- AICOS generellt förbättrar alla AI-svar.
- AICOS generellt förhindrar hallucinationer/fabrikation.
- effekterna generaliserar till andra modeller, domäner eller prompts.
- någon enskild regel i Council-systemet ensam orsakade resultaten.
- användare generellt föredrar eller litar mer på MED-svaren.
- den planerade Del B-bedömningen lyckades, eftersom den inte genomfördes.
- v3.4-fixar har verifierats; snapshotet säger uttryckligen att de inte har det.

CONFIDENCE:
MEDIUM-HIGH