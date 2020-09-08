class BlaaResept extends Resepter {

  public BlaaResept(Legemiddel middel, Lege lege, int pasientID, int reit){
    super(middel, lege, pasientID, reit);
  }

  public String farge() {
    return "blaa";
  }

  public double prisAaBetale() {
    return (this.hentLegemiddel().hentPris() * 0.25);
  }
}
