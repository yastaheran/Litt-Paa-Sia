abstract class HvitResept extends Resepter {

  public HvitResept(Legemiddel middel, Lege lege, Pasient pasient, int reit) {
    super(middel, lege, pasient, reit);
  }

  public String farge() {
    return "hvit";
  }
}
