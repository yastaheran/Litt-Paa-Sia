## Del A: Klassehierarki
Tegn klassehierarkiet (inkludert grensesnitt) til de forskjellige klassene som skal skrives. Det er viktig at du leser hele oppgaveteksten før du løser denne oppgaven!

## Del B: Lenkeliste
I denne oppgaven skal vi basere oss på grensesnittet Liste<T>. Skriv klassen Lenkeliste<T> som implementerer Liste<T>. Vi skal enkelt kunne sette inn elementer på slutten av listen og ta ut fra starten slik at det første elementet som ble satt inn
også er det første som blir tatt ut. På denne måten kan listen benyttes som en kø (First in, First out). Metoden leggTil (T x) skal altså sette inn et element på slutten av listen, mens fjern() skal fjerne og returnere elementet på starten av listen. I tillegg skal det finnes overlastede(overloaded) metoder for å sette, legge til og fjerne på gitte plasser:

* Metoden sett(int pos, T x) skal sette inn elementet på en gitt posisjon og overskrive det som var der fra før av.
* Metoden leggTil(int pos, T x) skal legge inn et nytt element i listen og skyve neste element ett hakk lenger bak.
* Metoden fjern(int pos) skal fjerne på gitt indeks i listen.

Til sist skal du også implementere metodene stoerrelse() og hent(int pos), der sistnevnte henter ut et element (uten å fjerne det fra lista) på oppgitt indeks (husk å telle fra indeks 0 og oppover).
