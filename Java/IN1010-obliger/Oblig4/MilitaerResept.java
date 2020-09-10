class MilitaerResept extends HvitResept {

  public MilitaerResept(Legemiddel middel, Lege lege, Pasient pasient, int reit) {
    super(middel, lege, pasient, reit);
  }

  public double prisAaBetale() {
    return 0.00;
  }
}
