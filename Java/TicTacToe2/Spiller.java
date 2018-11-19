public abstract class Spiller {
    protected int[] forsok = new int[2];
    protected int spiller;
    
    public Spiller(int spiller){
        this.spiller = spiller;
    }

    public abstract void Spill(Board board);

    public abstract void Try(Board board);

    public boolean checkTry(int[] forsok, Board board){
        if(board.getPosisjon(forsok) == 0) {
            return true;
        } else {
            return false;
        }
    }
}
