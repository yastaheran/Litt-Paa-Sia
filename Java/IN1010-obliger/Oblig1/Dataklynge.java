import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Dataklynge {
  private ArrayList<Rack> rackList = new ArrayList<Rack>();
  private int maxNodeRack;

  /* Oppgave 1-3
    Konstruktoeren tar imot maks antall noder pr rack
  public Dataklynge(int max) {
    this.maxNodeRack = max;
  } */

  /* Oppgave 4
    Konstruktoeren tar imot filnavn
  */
  public Dataklynge(String filnavn) {
    this.lesFil(filnavn);
  }

  private void lesFil(String filnavn) {
    try {
      Scanner leser =  new Scanner(new File(filnavn));

      while(leser.hasNextLine()) {
        String linje =  leser.nextLine();
        String[] info = linje.split(" ");

        if(info.length == 1) {
          this.maxNodeRack = Integer.parseInt(info[0]);
        } else {
          this.addNodeToRack(Integer.parseInt(info[0]), Integer.parseInt(info[1]));
        }
      }
    } catch (FileNotFoundException e) {
      System.out.println("Fil ikke funnet");
      return;
    }
  }

  public void addNodeToRack(int nodeMinne, int nodeProsessor) {
    if(rackList.size() != 0 && rackList.get(rackList.size()-1).getRackSize() < maxNodeRack) {
      rackList.get(rackList.size()-1).addNode(nodeMinne, nodeProsessor);
    } else {
      Rack nyRack = new Rack();
      nyRack.addNode(nodeMinne, nodeProsessor);
      rackList.add(nyRack);
    }
  }

  public int antProsessorer() {
    int ant = 0;

    for(int i = 0; i < rackList.size(); i++) {
      ant += rackList.get(i).getAntProsessorer();
    }

    return ant;
  }

  public int noderMedNokMinne(int paakrevdMinne) {
    int moeterKrav = 0;

    for(int i = 0; i < rackList.size(); i++) {
      moeterKrav += rackList.get(i).getAntNodeNokMinne(paakrevdMinne);
    }

    return moeterKrav;
  }

  public int antRacks() {
    return rackList.size();
  }
}
