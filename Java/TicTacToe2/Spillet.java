import java.util.Scanner;
public class Spillet {
    private Board board;
    private int tur=1, hvem=1;
    private Spiller spiller1, spiller2;
    public Scanner input = new Scanner(System.in);

    public Spillet(){
        board = new Board();
        startSpillere();
        while(Spill());
    }

    public void startSpillere(){
        System.out.println("Spiller 1: ");
        if(velgSpiller() == 1) {
            this.spiller1 = new SpillerPerson(1);
        } else {
            this.spiller1 = new SpillerDatamaskin(1);
        }
        System.out.println("----------------------");
        System.out.println("Spiller 2: ");
        if(velgSpiller() == 1) {
            this.spiller2 = new SpillerPerson(2);
        } else {
            this.spiller2 = new SpillerDatamaskin(2);
        }
    }

    public int velgSpiller(){
        int valg=0;
        do {
            System.out.println("1. Person1");
            System.out.println("2. DATAMASKIN\n");
            System.out.print("Valg: ");
            valg = input.nextInt();

            if(valg != 1 && valg != 2) {
                System.out.println("Ugyldig valg! Proeve igjen.");
            }
        }
        while(valg != 1 && valg != 2);
        return valg;
    }

    public boolean Spill(){
        board.showBoard();
        if(vant() == 0 ){
            System.out.println("----------------------");
            System.out.println("\nTur " + tur);
            System.out.println("Det er spiller" + hvem() + " sin tur");

            if(hvem()==1) {
                spiller1.Spill(board);
            } else {
                spiller2.Spill(board);
            }
            if(board.fullBoard()) {
                System.out.println("Likt!");
                return false;
            }
            hvem++;
            tur++;
            return true;
        } else {
            if(vant() == -1) {
                System.out.println("Spiller 1 vant!");
            } else {
                System.out.println("Spiller 2 vant!");
            }
            return false;
        }
    }

    public int hvem(){
        if(hvem%2 == 1) {
            return 1;
        } else {
            return 2;
        }
    }

    public int vant(){
        if(board.sjekkLinjer() == 1)
            return 1;
        if(board.sjekkKolonner() == 1)
            return 1;
        if(board.sjekkDiagonal() == 1)
            return 1;
        if(board.sjekkLinjer() == -1)
            return -1;
        if(board.sjekkKolonner() == -1)
            return -1;
        if(board.sjekkDiagonal() == -1)
            return -1;
        return 0;
    }
}
