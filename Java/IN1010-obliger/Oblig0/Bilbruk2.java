/**
  Lag et program (en klasse med en main-metode) som du kaller BilBruk2, som
  oppretter en bil med et bilnummer og som til slutt kaller skriv-metoden i
  dette bil-objektet.
*/

public class Bilbruk2 {
  public static void main(String args[]) {
    Bil2 bil =  new Bil2("Komplett");
    bil.printUt();
  }
}
