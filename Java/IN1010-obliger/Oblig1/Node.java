public class Node {
  private int minneStr;     // Storrelse i GB
  private int prosessorAnt; // Maks antall prosessorer

  public Node(int minne, int prosessorer) {
    this.minneStr = minne;
    this.prosessorAnt = prosessorer;
  }

  public int getProsessorAnt() {
    return this.prosessorAnt;
  }

  public int getMinneStr() {
    return this.minneStr;
  }
}
