public class TestResepter {
  public static void main(String args[]) {

    Narkotisk nark = new Narkotisk("Kokain",1000.00,50.00,6);
    Vanedannende vane = new Vanedannende("Vicodin",299.00,60.00,5);
    Vanlig vanlig = new Vanlig("P-piller", 199.0, 540.00);

    Lege lege = new Lege("Lege Ann-Helen");
    Lege lege2 = new Lege("Lege Marie");
    Lege lege3 = new Lege("Lege Beate");

    BlaaResept br = new BlaaResept(vane, lege, 90265, 10);
    MilitaerResept mr = new MilitaerResept(nark, lege2, 90264, 5);
    PResept pr = new PResept(vanlig, lege3, 90265);

    /* Tester resept */
    System.out.println("Test av BlaaResept.");
    testPris(br, 74.75);
    System.out.println();
    testFarge(br, "blaa");
    System.out.println();
    System.out.println("Test av 'printInfo()'.");
    br.printInfo();
    System.out.println("Test av 'printInfo()' utført.");
    System.out.println();
    System.out.println();

    /* Tester resept */
    System.out.println("Test av MilitaerResept.");
    testPris(mr, 0.00);
    System.out.println();
    testFarge(mr, "hvit");
    System.out.println();
    System.out.println("Test av 'printInfo()'.");
    mr.printInfo();
    System.out.println("Test av 'printInfo()' utført.");
    System.out.println();
    System.out.println();

    /* Tester av PResept */
    System.out.println("Test av PResept.");
    testPris(pr, 91.00);
    System.out.println();
    testFarge(pr, "hvit");
    System.out.println();
    System.out.println("Test av 'printInfo()'.");
    pr.printInfo();
    System.out.println("Test av 'printInfo()' utført.");
  }

  public static void testPris(Resepter testobj, double forventet) {
    System.out.println("Test av metode 'prisAaBetale()'");

    if(testobj.prisAaBetale() == forventet) {
      System.out.println("\nprisAaBetale() - Success");
    } else {
      System.out.println("\nprisAaBetale() - Failed");
    }
  }

  public static void testFarge(Resepter testobj, String forventet) {
    System.out.println("Test av metode 'farge()'");

    if(testobj.farge() == forventet) {
      System.out.println("\nfarge() - Success");
    } else {
      System.out.println("\nfarge() - Failed");
    }
  }
}
