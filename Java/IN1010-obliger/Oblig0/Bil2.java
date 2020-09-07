/**
  Lag en ny bilklasse Bil2 basert på bil-klassen fra oppgave 1 slik at alle
  biler får et bilnummer (en String). Når programmet oppretter et bil-objekt
  skal bilnummeret få verdi ved hjelp av konstruktøren til klassen. Modifiser
  skriv-metoden slik at den skriver ut nummeret på bilen.
*/
import java.util.*;

public class Bil2 {
  private String bilnr;

  public Bil2(String nr) {
    this.bilnr = nr;
  }

  public void setBilnr(String nummer) {
    this.bilnr = nummer;
  }

  public void printUt() {
    System.out.println("Mitt bilnr er: ''" + this.bilnr + "''");
  }
}
