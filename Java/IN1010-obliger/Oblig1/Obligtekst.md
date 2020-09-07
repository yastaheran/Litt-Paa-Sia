## Programdesign
### Klassen Node
Klassen skal kunne initiere nye objekter med ønsket minnestørrelse og prosessorantall, og for øvrig tilby tjenester (metoder) som trengs i andre deler av programmet.
### Klassen Rack
Klassen Rack skal lagre Node-objektene som hører til et rack i en liste. Vi skal kunne legge til noder i racket hvis det er færre enn maks antall noder der fra før. For enkelhets skyld skal vi
anta at hvert rack i dataklyngen har plass til like mange noder. Opprett andre instansvariable og metoder etter behov.
### Klassen Dataklynge
Klassen Dataklynge skal holde rede på en liste med racks, og må tilby en metode som tar imot et nodeobjekt og plasserer det i et rack med ledig plass. Hvis alle rackene er fulle, skal det lages
et nytt Rack-objekt som legges inn i listen, og noden plasseres i det nye racket. *Tips: Det kan være lurt å ta inn antall noder per rack i konstruktøren til Dataklynge.*

## 1. Klasser
Skriv klassene beskrevet under “Programdesign”. Der det ikke er oppgitt hva slags datatype som
skal brukes (for eksempel ved valg av listetype) forventes det at du selv gjør fornuftige valg og
begrunner disse gjennom kommentarer i koden.
