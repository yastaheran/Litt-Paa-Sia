public class Stabel<T> extends Lenkeliste<T> {

  public void leggPaa(T x) {
    this.leggTil(x);
  }

  public T taAv() {
    return fjern(this.stoerrelse()-1);
  }
}
