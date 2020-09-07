/**
  3a) Lag en ny bilklasse Bil3 basert på bil-klassen fra oppgave 2 slik at alle
  biler nå får en metode hentNummer.
*/

import java.util.*;

public class Bil3 {
  private String bilnr;

  public Bil3(String nr) {
    this.bilnr = nr;
  }

  public void setBilnr(String nummer) {
    this.bilnr = nummer;
  }

  public String hentNummer() {
    return this.bilnr;
  }

  public void printUt() {
    System.out.println("Mitt bilnr er: '" + this.bilnr + "'");
  }
}
