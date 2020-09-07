/**
  3b) Lag en klasse Person. Alle personer skal eie en bil, og når programmet
  oppretter et person-objekt skal en referanse til personens bil (av klassen
  Bil3) være parameter til konstruktøren. Alle Person-objekter skal inneholde
  en metode som skriver ut bilnummeret til bilen som personen eier.
*/

public class Person {
  Bil3 minBil;

  public Person(Bil3 bil) {
    this.minBil = bil;
  }

  public void mittBilNr() {
    this.minBil.printUt();
  }
}
