class MilitaerResept extends HvitResept {

  public MilitaerResept(Legemiddel middel, Lege lege, int pasientID, int reit) {
    super(middel, lege, pasientID, reit);
  }

  public double prisAaBetale() {
    return 0.00;
  }
}
