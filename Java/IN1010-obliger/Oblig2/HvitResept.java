abstract class HvitResept extends Resepter {

  public HvitResept(Legemiddel middel, Lege lege, int pasientID, int reit) {
    super(middel, lege, pasientID, reit);
  }

  public String farge() {
    return "hvit";
  }
}
