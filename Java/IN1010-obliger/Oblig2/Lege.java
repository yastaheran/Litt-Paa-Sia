class Lege {
  private String navn;

  public Lege(String navn) {
   this.navn = navn;
  }

  public String hentNavn(){
    return this.navn;
  }

  public void printInfo() {
    System.out.println("Legens navn: " + this.hentNavn());
  }
}
