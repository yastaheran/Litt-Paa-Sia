class PResept extends HvitResept {

  public PResept(Legemiddel middel, Lege lege, Pasient pasient) {
    super(middel, lege, pasient, 3);
  }

  public double prisAaBetale() {
    double legemiddelPris = this.hentLegemiddel().hentPris();
    return (legemiddelPris <= 108.00) ? 0.00 : (legemiddelPris - 108.00);
  }
}
