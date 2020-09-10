class BlaaResept extends Resepter {

  public BlaaResept(Legemiddel middel, Lege lege, Pasient pasient, int reit){
    super(middel, lege, pasient, reit);
  }

  public String farge() {
    return "blaa";
  }

  public double prisAaBetale() {
    return (this.hentLegemiddel().hentPris() * 0.25);
  }
}
