import java.util.Scanner;
public class SpillerPerson extends Spiller{
    public Scanner input = new Scanner(System.in);

    public SpillerPerson(int spiller){
        super(spiller);
        this.spiller = spiller;
        System.out.println("Spiller 'SpillerPerson' laget!");
    }

    @Override
    public void Spill(Board board){
        Try(board);
        board.setPosisjon(forsok, spiller);
    }

    @Override
    public void Try(Board board) {
        do {
            do {
                System.out.print("Rad: ");
                forsok[0] = input.nextInt();
                if( forsok[0] > 3 ||forsok[0] < 1) {
                    System.out.println("Ugyldig rad. It's 1, 2 or 3");
                }
            } while( forsok[0] > 3 ||forsok[0] < 1);
            do {
                System.out.print("Kolonne: ");
                forsok[1] = input.nextInt();
                if(forsok[1] > 3 ||forsok[1] < 1)
                    System.out.println("Ugyldig kolonne. É 1, 2 or 3");
            }while(forsok[1] > 3 ||forsok[1] < 1);
            forsok[0]--;
            forsok[1]--;
            if(!checkTry(forsok, board))
                System.out.println("Plasssen er tatt. Proev igjen.");
        }
        while(!checkTry(forsok, board));
    }
}
