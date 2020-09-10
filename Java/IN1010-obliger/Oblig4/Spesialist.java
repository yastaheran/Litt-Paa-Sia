class Spesialist extends Lege implements Godkjenningsfritak {
  int kontrollID;

  public Spesialist(String navn, int kontrollID) {
    super(navn);
    this.kontrollID = kontrollID;
  }

  @Override
    public int hentKontrollID(){
      return this.kontrollID;
    }

  @Override
    public void printInfo() {
      System.out.println("Legens navn: " + this.hentNavn());
      System.out.println("Legens kontroll ID: " + this.hentKontrollID());
    }
}
