/**
  3c) Lag et program BilBruk3 der main-metoden først oppretter en bil og
  deretter en person som eier denne bilen. Til slutt skal programmet kalle
  skriv-metoden i dette Person-objektet.
*/

public class Bilbruk3 {
  public static void main(String args[]) {
    Bil3 nyBil = new Bil3("Komplett");
    Person eier = new Person(nyBil);

    eier.mittBilNr();
  }
}
