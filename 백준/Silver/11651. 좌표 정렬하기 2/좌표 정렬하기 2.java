import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    class Node implements Comparable<Node> {
      int x;
      int y;

      public Node(int x, int y) {
        this.x = x;
        this.y = y;
      }

      public int compareTo(Node target) {
        if (target.y == this.y) {
          return this.x < target.x ? -1 : 1;
        }
        return this.y < target.y ? -1 : 1;
      }

      public String toString() {
        return x + " " + y;
      }
    }

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int r = Integer.parseInt(st.nextToken());
    PriorityQueue<Node> pq = new PriorityQueue<>();

    for (int i=0; i<r; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      Node node = new Node(x, y);
      pq.add(node);
    }

    while(!pq.isEmpty()) {
      Node node = pq.poll();
      System.out.println(node.toString());
    }
  }
}
