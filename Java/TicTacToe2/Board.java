public class Board {
    private int[][] Board= new int[3][3]; //Array som holder paa posisjonene til brikkene
    
    public Board(){
        clearBoard();
    }

    public void clearBoard(){
        for(int linje=0 ; linje<3 ; linje++)
            for(int kolonne=0 ; kolonne<3 ; kolonne++)
                Board[linje][kolonne]=0;
    }

    public void showBoard(){
        System.out.println();
        for(int linje=0 ; linje<3 ; linje++){
            for(int kolonne=0 ; kolonne<3 ; kolonne++){
                if(Board[linje][kolonne]==-1){
                    System.out.print(" X ");
                }
                if(Board[linje][kolonne]==1){
                    System.out.print(" O ");
                }
                if(Board[linje][kolonne]==0){
                    System.out.print("   ");
                }

                if(kolonne==0 || kolonne==1)
                    System.out.print("|");
            }
            System.out.println();
        }
    }

    public int getPosisjon(int[] forsok){
        return Board[forsok[0]][forsok[1]];
    }

    public void setPosisjon(int[] forsok, int spiller){
        if(spiller == 1)
            Board[forsok[0]][forsok[1]] = -1;
        else
            Board[forsok[0]][forsok[1]] = 1;
    }

    public int sjekkLinjer(){
        for(int linje=0 ; linje<3 ; linje++){
            if( (Board[linje][0] + Board[linje][1] + Board[linje][2]) == -3) {
                return -1;
            }
            if( (Board[linje][0] + Board[linje][1] + Board[linje][2]) == 3) {
                return 1;
            }
        }
        return 0;
    }

    public int sjekkKolonner(){
        for(int kolonne=0 ; kolonne<3 ; kolonne++){
            if( (Board[0][kolonne] + Board[1][kolonne] + Board[2][kolonne]) == -3) {
              return -1;
            }
            if( (Board[0][kolonne] + Board[1][kolonne] + Board[2][kolonne]) == 3) {
              return 1;
            }
        }
        return 0;
    }

    public int sjekkDiagonal(){
        if( (Board[0][0] + Board[1][1] + Board[2][2]) == -3) {
          return -1;
        }
        if( (Board[0][0] + Board[1][1] + Board[2][2]) == 3) {
          return 1;
        }
        if( (Board[0][2] + Board[1][1] + Board[2][0]) == -3)  {
          return 1;
        }
        if( (Board[0][2] + Board[1][1] + Board[2][0]) == 3) {
          return 1;
        }
        return 0;
    }

    public boolean fullBoard(){
        for(int linje=0 ; linje<3 ; linje++)
            for(int kolonne=0 ; kolonne<3 ; kolonne++)
                if( Board[linje][kolonne]==0 )
                    return false;
        return true;
    }
}
