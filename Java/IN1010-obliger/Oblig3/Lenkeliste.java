class Lenkeliste<T> implements Liste<T>{

  public class Node{
    Node neste = null;
    T data;

    Node(T x){
      this.data = x;
    }
  }
  Node start = new Node(null);

  public void leggTil(T x){
    if (start.neste == null){
      start.neste = new Node(x);
      System.out.println(start.neste.data);
    } else {
      Node temp = start;

      while (temp.neste != null){
        temp = temp.neste;
      }

      temp.neste = new Node(x);
    }
  }

  public T fjern(){
    if (start.neste == null){
      throw new UgyldigListeIndeks(-1);
    } else {
      Node temp = start.neste;
      start.neste = temp.neste;
      return temp.data;
    }
  }

  public void sett(int pos, T x){
    if (pos < 0 || pos >= this.stoerrelse()){
      throw new UgyldigListeIndeks(pos);
    }

    Node temp = start;

    for (int i = 0; i < pos; i++){
      temp = temp.neste;
    }

    temp.neste.data = x;
  }

  public void leggTil(int pos, T x){
    if (pos < 0 || pos > this.stoerrelse()){
      throw new UgyldigListeIndeks(pos);
    }

    if (pos == 0){
      Node temp = new Node(x);
      temp.neste = start.neste;
      start.neste = temp;
    } else {
      Node temp = start;

      for (int i = 0; i < pos; i++){
        temp = temp.neste;
      }

      Node ny = new Node(x);
      ny.neste=temp.neste;
      temp.neste=ny;
    }
  }

  public T fjern(int pos){
    if (pos < 0 || pos >= this.stoerrelse()){
      throw new UgyldigListeIndeks(pos);
    }

    Node temp = start;
    for (int i = 0; i < pos; i++){
      temp = temp.neste;
    }

    Node fjernes = temp.neste;
    temp.neste = fjernes.neste;
    return fjernes.data;
  }

  public int stoerrelse(){
    Node temp = start;
    int n = 0;

    while (temp.neste != null){
      n++;
      temp = temp.neste;
    }

    return n;
  }

  public T hent(int pos){
    if (pos < 0 || pos >= this.stoerrelse()){
      throw new UgyldigListeIndeks(pos);
    }

    Node temp = start.neste;

    for (int i = 0; i < pos; i++){
      temp = temp.neste;
    }

    return temp.data;
  }
}
