import java.util.ArrayList;

public class Rack {
  private ArrayList<Node> nodeListe = new ArrayList<Node>();
  private int antProsessorer;

  public void addNode(int minne, int prosessor) {
    Node nyNode = new Node(minne, prosessor);
    this.nodeListe.add(nyNode);
    this.antProsessorer += prosessor;
  }

  public int getRackSize() {
    return this.nodeListe.size();
  }

  public int getAntProsessorer() {
    return antProsessorer;
  }

  public int getAntNodeNokMinne(int krav) {
    int moeterKrav = 0;
    for(int i = 0; i < nodeListe.size(); i++) {
      if(nodeListe.get(i).getMinneStr() >= krav) {
        moeterKrav++;
      }
    }
    return moeterKrav;
  }
}
