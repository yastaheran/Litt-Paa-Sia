public class SortertLenkeliste<T extends Comparable<T>> extends Lenkeliste{
  public SortertLenkeliste() {
    super();
  }

  public void leggTil(T x) {
    Node ny = new Node(x);

    if (start.neste == null){
      start.neste = ny;
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

  public T fjern() {
    return fjern(this.stoerrelse()-1);
  }

  public void leggTil(int pos, T x){
    throw new UnsupportedOperationException("Denne kan ikke brukes.");
  }

  public T fjern(int pos){
    throw new UnsupportedOperationException("Denne kan ikke brukes.");
  }
}
