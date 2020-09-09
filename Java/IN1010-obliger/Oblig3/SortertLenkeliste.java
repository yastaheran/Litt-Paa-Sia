public class SortertLenkeliste<T extends Combarable<T>> extends Lenkeliste{
  @Override
  public void leggTil(T x) {
    Node ny = new Node(x);
    if(start.neste == null) {
        start = ny;
    } else {
      Node temp = start;
      
      while (temp.neste != null && temp.neste.data.compareTo(x) < 0){
        temp = temp.neste;
      }

      if (temp.neste != null){
        ny.neste = temp.neste;
      }

      temp.neste = ny;
    }
  }

  @Override
  public T fjern() {
    return fjern(this.stoerrelse()-1);
  }

  @Override
  public void leggTil(int pos, T x){
    throw new UnsupportedOperationException("Denne kan ikke brukes.");
  }

  @Override
  public T fjern(int pos){
    throw new UnsupportedOperationException("Denne kan ikke brukes.");
  }
}
