class Lege implements Comparable<Lege>{
  private String navn;
  private Lenkeliste<Resepter> utskrevedeResepter;

  public Lege(String navn) {
   this.navn = navn;
  }

  public String hentNavn(){
    return this.navn;
  }

  public void printInfo() {
    System.out.println("Legens navn: " + this.hentNavn());
  }

  public int compareTo(Lege lege2) {
    return (this.navn.compareTo(lege2.hentNavn()));
  }

  public Lenkeliste<Resepter> hentUtReseptListe() {
    return this.utskrevedeResepter;
  }

  public BlaaResept skrivBlaaResept(Legemiddel legemiddel, Pasient pasient, int reit) {
    if(legemiddel instanceof Narkotisk) {
      throw new UlovligUtskrift(this, legemiddel, pasient);
    }

    BlaaResept br = new BlaaResept(legemiddel, this, pasient, reit);
    utskrevedeResepter.leggTil(br);
    return br;
  }

  public MilitaerResept skrivMilitaerResept(Legemiddel legemiddel, Pasient pasient, int reit) {
    if(legemiddel instanceof Narkotisk) {
      throw new UlovligUtskrift(this, legemiddel, pasient);
    }

    MilitaerResept mr = new MilitaerResept(legemiddel, this, pasient, reit);
    utskrevedeResepter.leggTil(mr);
    return mr;
  }

  public PResept skrivPResept(Legemiddel legemiddel, Pasient pasient) {
    if(legemiddel instanceof Narkotisk) {
      throw new UlovligUtskrift(this, legemiddel, pasient);
    }

    PResept pr = new PResept(legemiddel, this, pasient);
    utskrevedeResepter.leggTil(pr);
    return pr;
  }
}
