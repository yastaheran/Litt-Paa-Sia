class Vanedannende extends Legemiddel{
  private int styrke;

  public Vanedannende(String navn, double pris, double virkestoff, int styrke) {
    super(navn, pris, virkestoff);
    this.styrke = styrke;
  }

  public int hentVanedannendeStyrke() {
    return this.styrke;
  }

  public void printInfo(){
    System.out.println("\nLegemiddelets ID: " + this.hentID());
    System.out.println("Legemiddelets navn: " + this.hentNavn());
    System.out.println("Legemiddelets pris [kr]: " + this.hentPris());
    System.out.println("Mengde virkestoff [mg] i legemiddelet: " + this.hentVirkestoff());
    System.out.println("Legemiddelets vanedannende styrke: " + this.hentVanedannendeStyrke());
  }
}
