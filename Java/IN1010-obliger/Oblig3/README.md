## Lenkeliste
I denne oppgaven skal vi basere oss på grensesnittet Liste<T>. Skriv klassen Lenkeliste<T> som implementerer Liste<T>. Vi skal enkelt kunne sette inn elementer på slutten av listen og ta ut fra starten slik at det første elementet som ble satt inn
også er det første som blir tatt ut. På denne måten kan listen benyttes som en kø (First in, First out). Metoden leggTil (T x) skal altså sette inn et element på slutten av listen, mens fjern() skal fjerne og returnere elementet på starten av listen. I tillegg skal det finnes overlastede(overloaded) metoder for å sette, legge til og fjerne på gitte plasser:

* Metoden sett(int pos, T x) skal sette inn elementet på en gitt posisjon og overskrive det som var der fra før av.
* Metoden leggTil(int pos, T x) skal legge inn et nytt element i listen og skyve neste element ett hakk lenger bak.
* Metoden fjern(int pos) skal fjerne på gitt indeks i listen.

Til sist skal du også implementere metodene stoerrelse() og hent(int pos), der sistnevnte henter ut et element (uten å fjerne det fra lista) på oppgitt indeks (husk å telle fra indeks 0 og oppover).

Når vi arbeider med indekser kan vi møte på feil dersom vi forsøker å nå en indeks som ikke eksisterer. Gyldige indekser i listen vil være være som vi er vant til i en array eller en ArrayList, altså fra og med 0 og til, men ikke med, listens størrelse. For å ta høyde for eventuelle feil skal vi en egendefinerte unntaksklasse.

## Stabel
En stabel er en liste som fungerer litt annerledes enn en vanlig lenkeliste. Når man legger et element inn, skal det være det første som skal hentes ut.

Skriv klassen Stabel<T>. Klassen skal arve fra Lenkeliste<T>, men skal i tillegg ha metodene leggPaa (T x) og taAv(). Disse metodene skal henholdsvis legge til og fjerne elementer fra slutten av listen, slik at det siste elementet som legges inn er det første som tas ut (Last in, First out). Merk: Det forventes her at du tar i bruk metodene som er arvet fra Lenkeliste<T>.

## Sortert Lenkeliste
Skriv klassen SortertLenkeliste<T extends Comparable<T> >. Denne listen arver også fra Lenkeliste<T>, men vi ønsker at listen skal være sortert og krever derfor at elementer som settes inn skal være sammenlignbare. Kall på leggTil(T x) skal altså sette inn elementer i sortert rekkefølge (fra minst til størst), og når vi bruker fjern()-metoden (uten parametere) skal det største elementet tas ut.

Du skal nå begrense mulighetene for å sette inn elementer på en vilkårlig posisjon, slik at listen forblir sortert. Dette kan gjøres ved å la SortertLenkeliste overskrive metodene sett(int pos, T x) og leggTil(int pos, T x). De nye implementasjonene skal ikke sette inn elementet, men i stedet kun kaste et unntak som finnes i Java fra før av: UnsupportedOperationException.
