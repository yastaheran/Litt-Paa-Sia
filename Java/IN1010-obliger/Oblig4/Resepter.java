abstract class Resepter {
  private Legemiddel middel;
  private Lege lege;
  private Pasient pasient;
  private int reit;
  private int id;
  private int idCounter;

  public Resepter(Legemiddel middel, Lege lege, Pasient p, int reit) {
    this.middel = middel;
    this.lege = lege;
    this.pasient = p;
    this.reit = reit;
    this.id = idCounter;
    this.idCounter++;
  }

  public int hentID() {
    return this.id;
  }

  public Legemiddel hentLegemiddel(){
    return this.middel;
  }

  public Lege hentLege() {
    return this.lege;
  }

  public int hentPasientID(){
    return this.pasient.hentID();
  }

  public int hentReit(){
    return this.reit;
  }

  public boolean bruk(){
    if(this.reit > 0) {
      this.reit--;
      return true;
    }
    return false;
  }

  abstract public String farge();
  abstract public double prisAaBetale();

  public void printInfo() {
    System.out.println("\nReseptens ID: " + this.hentID());
    System.out.println("\nLegemiddelets navn: " + this.hentLegemiddel().hentNavn());
    System.out.println("\nLegemiddelets pris [kr]: " + this.hentLegemiddel().hentPris());
    System.out.println("\nLegemiddelets pris etter reseptrabatt [kr]: " + this.prisAaBetale());
    System.out.println("\nReseptens farge: " + this.farge());
    System.out.println("\nLegens navn: " + this.hentLege().hentNavn());
    System.out.println("\nPasientens ID: " + this.hentPasientID());
    System.out.println("\nReit: " + this.hentReit());
  }
}
