## Del A: Legemidler
Legemidler deles inn i tre kategorier, narkotisk, vanedannende og vanlige legemidler. Et legemiddel har et navn, en ID og en pris. I tillegg må vi for alle legemidler kunne vite hvor mye virkestoff (mg) det inneholder totalt. Prisen og virkestoffet skal lagres som flyttall.
Et legemiddel skal være en av subtypene Narkotisk, Vanedannende, eller Vanlig legemiddel. Det er stor forskjell på legemidler av disse tre typene, men i denne oppgaven skal vi bare ta hensyn til følgende krav for de forskjellige typene legemidler:
* Narkotisk legemiddel har et heltall som sier hvor sterkt narkotisk det er.
* Vanedannende legemiddel har et heltall som sier hvor vanedannende det er.
* Vanlig legemiddel har ingen tilleggsegenskaper (annet enn klassens navn).

Skriv et testprogram TestLegemiddel. I denne klassen skal du opprette et objekt av hver av subklassene du har skrevet. Deretter skal du gjøre enkle enhetstester der du tester alle egenskapene til en instans før du går videre og gjør det samme for neste instans.

## Del B: Resepter
En Resept har en ID. I tillegg skal en resept ha en referanse til et legemiddel, en referanse til den legen som har skrevet ut resepten, og ID-en til den pasienten som eier resepten. En resept har et antall ganger som er igjen på resepten (kalles reit). Hvis antall ganger igjen er 0, er resepten ugyldig. I denne oppgaven skal vi forholde oss til ulike typer resepter. De to hovedkategoriene er hvite og blå resepter.

### Hvit resept
Hvite resepter har i seg selv ingen nye egenskaper (utover et annet klassenavn), men det skal være mulig å opprette instanser av dem. Derimot finnes det to subtyper av hvit resept: Militærresepter og P-resepter.

**Militærresepter** utgis til vernepliktige i tjeneste. Som en forenkling sier vi at militærresepter alltid gir en 100% rabatt på prisen til et legemiddel.
**P-resepter** gir unge en rabatt på prevensjonsmidler. Denne rabatten er statisk og gjør at brukeren betaler 108 kroner mindre for legemiddelet. **Merk:** Brukeren aldri kan betale mindre enn 0 kroner. I tillegg til rabatten har P-resepter den egenskapen at de alltid utskrives med 3 reit.

### Blå resept
Det er stor forskjell på vanlige (hvite) og blå resepter (blant annet er utstedelsen av en blå resept forbundet med en del kontroller), men igjen skal vi gjøre en forenkling og si at bare prisen som betales er forskjellig: Blå resepter er alltid sterkt subsidiert, og for enkelhets skyld sier vi her at de har 75% rabatt slik at pasienten må betale 25% av prisen på legemidlet.

Klassen Resept skal ha følgende metoder som henter relevant data: hentId, hentLegemiddel (henter tilhørende Legemiddel), hentLege (henter utskrivende Lege), hentPasientId og hentReit. I tillegg skal klassen ha følgende metoder: public boolean bruk: Forsøker å bruke resepten én gang. Returner false om resepten alt er oppbrukt, ellers returnerer den true. abstract public String farge: Returnerer reseptens farge. Enten “hvit” eller "blaa". abstract public double prisAaBetale: Returnerer prisen pasienten må betale.

## Del C: Leger
Konstruktøren i Lege tar kun inn en String med legens navn. Lege skal ha en metode for å hente ut navnet til legen. Noen leger er Spesialister. Spesialister har fått godkjenningsfritak til å skrive ut resept på narkotiske legemidler. Å ha godkjenningsfritak kan gjelde for andre enn leger, så dette skal implementeres som et grensesnitt (interface). Alle som har godkjenningsfritak, har en kontroll ID, som kan hentes ut for å sjekke at godkjenningsfritaket ikke blir misbrukt. Spesialist skal arve fra Lege og skal i tillegg implementere følgende grensesnitt.

## Del D: Integrasjonstest
I denne delen skal du lage et hovedprogram som gjør det vi vil kalle en minimal integrasjonstest - vi skal altså teste hvordan de forskjellige delene av systemet fungerer sammen. Hovedprogrammet skal gjøre følgende:
* Opprette minimum en instans av hver eneste klasse og la disse inneholde nødvendige referanser til andre objekter.
* Skrive ut relevant informasjon om hvert enkelt objekt. (Her vil det lønne seg å ha overskrevet toString() metoden i alle klassene du har skrevet).
