class PResept extends HvitResept {

  public PResept(Legemiddel middel, Lege lege, int pasientID) {
    super(middel, lege, pasientID, 3);
  }

  public double prisAaBetale() {
    double legemiddelPris = this.hentLegemiddel().hentPris();
    return (legemiddelPris <= 108.00) ? 0.00 : (legemiddelPris - 108.00);
  }
}
