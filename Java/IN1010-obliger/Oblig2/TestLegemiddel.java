
class TestLegemiddel {
  public static void main(String args[]) {

    Narkotisk nark = new Narkotisk("Kokain",1000.00,50.00,6);
    Vanedannende vane = new Vanedannende("Vicodin",299.00,60.00,5);
    Vanlig vanlig = new Vanlig("Ibux", 199.0, 540.00);

    /* Tester for Narkotiske legemidler */
    testPris(nark);
    System.out.println("Test av metode 'printInfo()'.");
    nark.printInfo();
    System.out.println("Test av metode 'printInfo()' fullfoert.");

    /* Tester for Vanedannende legemidler */
    testPris(vane);
    System.out.println("Test av metode 'printInfo()'.");
    vane.printInfo();
    System.out.println("Test av metode 'printInfo()' fullfoert.");

    /* Tester for Vanlige legemidler */
    testPris(vanlig);
    System.out.println("Test av metode 'printInfo()'.");
    vanlig.printInfo();
    System.out.println("Test av metode 'printInfo()' fullfoert.");

  }

  public static void testPris(Legemiddel testobj) {
    System.out.println("Test av metode 'settNyPris'.");
    System.out.println("Forventet resultat: ");
    System.out.println("\n Pris [kr]: 19.00");
    testobj.settNyPris(19.00);

    //assertEquals(19.00, testobj.hentPris);
    if(testobj.hentPris() == 19.00) {
      System.out.println("settNyPris() - Success");
    } else {
      System.out.println("settNyPris() - Failed");
    }
  }
}
