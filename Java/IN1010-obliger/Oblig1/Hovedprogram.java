public class Hovedprogram {

  public static void main(String args[]) {
    String filnavn = args[0]; //Sender med filnavn som parameter
    Dataklynge dk = new Dataklynge(filnavn);

    /** Oppgave 3. Hovedprogram
    Dataklynge nyDK = new Dataklynge(12);

    for(int i = 0; i < 650; i++) {
      nyDK.addNodeToRack(64, 1);
    }

    for(int i = 0; i < 16; i++) {
      nyDK.addNodeToRack(1024, 2);
    } */

    int noder32GB = dk.noderMedNokMinne(32);
    int noder64GB = dk.noderMedNokMinne(64);
    int noder128GB = dk.noderMedNokMinne(128);
    int totProsessorer = dk.antProsessorer();
    int antRacks = dk.antRacks();

    System.out.println("Noder med minst 32GB: " + noder32GB);
    System.out.println("Noder med minst 64GB: " + noder64GB);
    System.out.println("Noder med minst 128GB: " + noder128GB);
    System.out.println("Totalt prosessor: " + totProsessorer);
    System.out.println("Antall Racks " + antRacks);

  }
}
