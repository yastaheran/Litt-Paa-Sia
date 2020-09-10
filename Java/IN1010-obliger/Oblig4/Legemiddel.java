abstract class Legemiddel {
  private String navn;
  private double pris;
  private double virkestoff;
  private int id;
  private static int countID = 0;

  public Legemiddel(String navn, double pris, double virkestoff) {
    this.navn = navn;
    this.pris = pris;
    this.virkestoff = virkestoff;
    this.id = countID;
    this.countID++;
  }

  public int hentID() {
    return this.id;
  }

  public String hentNavn() {
    return this.navn;
  }

  public double hentPris() {
    return this.pris;
  }

  public double hentVirkestoff() {
    return this.virkestoff;
  }

  public void settNyPris(double nyPris) {
    this.pris = nyPris;
  }

  public void printInfo(){
    System.out.println("\nLegemiddelets ID: " + this.hentID());
    System.out.println("Legemiddelets navn: " + this.hentNavn());
    System.out.println("Legemiddelets pris [kr]: " + this.hentPris());
    System.out.println("Mengde virkestoff [mg] i legemiddelet: " + this.hentVirkestoff());
  }
}
