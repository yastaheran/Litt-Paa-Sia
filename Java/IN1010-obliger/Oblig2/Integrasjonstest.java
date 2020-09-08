class Integrasjonstest {
  public static void main(String args[]) {
    /* Test score variabler */
    int numSuccess = 0;
    int numFailed = 0;

    /* Instanser */
    Narkotisk nark = new Narkotisk("Kokain",1000.00,50.00,6);
    Vanedannende vane = new Vanedannende("Vicodin",299.00,60.00,5);
    Vanlig vanlig = new Vanlig("P-piller", 199.0, 540.00);

    Lege lege = new Lege("Lege Ann-Helen");
    Spesialist lege2 = new Spesialist("Lege Marie", 240695);

    BlaaResept br = new BlaaResept(vane, lege2, 90265, 10);
    MilitaerResept mr = new MilitaerResept(nark, lege2, 90264, 5);
    PResept pr = new PResept(vanlig, lege, 90265);

    /* Tester */
    System.out.println("Tester hent-metoder for instanser");

    if(testFritak(lege2, 240695)) {
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testPrisMiddel(nark, 1000.00)) {
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testPrisResept(br, 74.75)) { //Test av BlaaResept
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testPrisResept(pr, 91.00)) {  //Test av HvitResept -> PResept
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testFarge(mr, "hvit")) {
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testReit(pr, 3)) {
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    if(testBrukResept(mr, true)) {
      numSuccess++;
      System.out.println("Success");
    } else {
      numFailed++;
      System.out.println("Failed");
    }

    System.out.println("Tester av hent-metoder for instanser fullført");
    System.out.println(numSuccess + " antall tester besto og " + numFailed + " antall tester feilet.");
    System.out.println();

    /* Test print-funksjonen til instansene */
    System.out.println("Starter test av print-metoder for instanser");
    System.out.println();

    System.out.println("Tester printInfo() for Narkotisk Legemiddel");
    nark.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Vanedannende Legemiddel");
    vane.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Vanlig Legemiddel");
    vanlig.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Blaa Resept");
    br.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for P-resept");
    pr.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Militaer Resept");
    mr.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Lege");
    lege.printInfo();
    System.out.println();

    System.out.println("Tester printInfo() for Spesialist");
    lege2.printInfo();

    System.out.println("Test av print-metoder for instanser fullført.");
  }

  public static boolean testFritak(Spesialist testobj, int forventet) {
    System.out.println("Tester hentKontrollID() for Spesialist");
    return forventet == testobj.hentKontrollID() ? true : false;
  }

  public static boolean testPrisMiddel(Legemiddel testobj, double forventet) {
    System.out.println("Tester hentPris() for Legemiddel");
    return forventet == testobj.hentPris() ? true : false;
  }

  public static boolean testPrisResept(Resepter testobj, double forventet) {
    System.out.println("Tester prisAaBetale() for Resept");
    return forventet == testobj.prisAaBetale() ? true : false;
  }

  public static boolean testFarge(Resepter testobj, String forventet) {
    System.out.println("Tester farge() for Resept");
    return forventet == testobj.farge() ? true : false;
  }

  public static boolean testReit(Resepter testobj, int forventet) {
    System.out.println("Tester hentReit() for Resept");
    return forventet == testobj.hentReit() ? true : false;
  }

  public static boolean testBrukResept(Resepter testobj, boolean forventet) {
    System.out.println("Tester bruk() for Resept");
    return forventet == testobj.bruk() ? true : false;
  }
}
