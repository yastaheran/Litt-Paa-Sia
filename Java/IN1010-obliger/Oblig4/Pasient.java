public class Pasient {
  private String navn;
  private String fodselsnummer;
  private int pasientID;
  private Stabel<Resepter> reseptliste;

  public Pasient(String navn, String fodselsnr) {
    this.navn = navn;
    this.fodselsnummer = fodselsnr;
    this.pasientID = pasientID;
    pasientID++;
    this.reseptliste = new Stabel<Resepter>();
  }

  public void leggTilResept(Resepter r) {
    reseptliste.leggPaa(r);
  }

  public Stabel<Resepter> hentUtReseptListe() {
    return this.reseptliste;
  }

  public int hentID() {
    return this.pasientID;
  }

  public String hentNavn(){
    return this.navn;
  }

  public String hentFodselsnr(){
    return this.fodselsnummer;
  }
}
