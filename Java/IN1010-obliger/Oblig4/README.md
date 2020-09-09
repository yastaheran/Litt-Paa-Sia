## Pasient
Skriv klassen Pasient.
En Pasient er en typisk bruker av resepter. Pasienten har et navn og et fødselsnummer-tekststreng. Når en ny pasient registreres skal denne i tillegg få en unik ID. Pasienter har også en liste over reseptene de har fått utskrevet. Siden pasienten ofte vil bruke en resept kort tid etter at den er utskrevet, bruker vi en Stabel<Resept> til å lagre pasientens resepter. Det skal både være mulig å legge til nye resepter og hente ut hele reseptlisten.

Endre klassene som tar inn en int pasientid til å ta inn en Pasient pasient.

## Itererbare lister
For å enkelt kunne løpe gjennom listene våre skal vi sørge for at de er itererbare. Dette skal gjøres “fra toppen” ved å modifisere grensesnittet fra Liste<T> slik at det utvider java-grensesnittet Iterable<T>. Det er her viktig å skille mellom grensesnittene Iterable og Iterator.
Iterable er et grensesnitt i Java som brukes av listene våre for å gjøre dem itererbare. Denne implementasjonen gjør blant annet at vi får lov til å skrive en for each-løkke som løper gjennom listen vår. Grensesnittet ser slik ut:

    interface Iterable<T> {
      Iterator<T> iterator();
    }

Iterator er et annet grensesnitt som beskriver selve iterator-objektet vi bruker for å gå gjennom listen. Siden alle lister ikke er like trengs det en egen Iterator-klasse som implementerer Iterator<T>, spesialtilpasset våre lister. Dette grensesnittet ser slik ut:

    interface Iterator<T> {
      boolean hasNext();
      T next();
      void remove();
    }
    
En fordel med implementasjonen av dette er at vi får tilgang til å bruke for-each-notasjon:
    for (E e : elementliste) {
       //Gjoer noe med e ...
    }
som egentlig er kortform for “så lenge iteratoren finner et et neste element i listen (hasNext() returnerer true), hent det ut (next()).”
