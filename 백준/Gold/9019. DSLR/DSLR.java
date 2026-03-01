import java.io.*;
import java.util.*;

public class Main {

  static class Node {
    int value;
    String history;

    public Node(int value, String history) {
      this.value = value;
      this.history = history;
    }

    public int getValue() {
      return value;
    }

    public String getHistory() {
      return history;
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

    while (T-- > 0) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());

      Queue<Node> queue = new LinkedList<>();
      Set<Integer> visited = new HashSet<>();
      queue.add(new Node(from, ""));
      visited.add(from);
      while (!queue.isEmpty()) {
        Node curr = queue.poll();
        if (curr.getValue() == to) {
          System.out.println(curr.getHistory());
          break;
        }

        int valueAfterD = doCommand(curr.getValue(), 'D');
        if (!visited.contains(valueAfterD)) {
          queue.add(new Node(valueAfterD, curr.getHistory()+"D"));
          visited.add(valueAfterD);
        }
        int valueAfterS = doCommand(curr.getValue(), 'S');
        if (!visited.contains(valueAfterS)) {
          queue.add(new Node(valueAfterS, curr.getHistory()+"S"));
          visited.add(valueAfterS);
        }
        int valueAfterL = doCommand(curr.getValue(), 'L');
        if (!visited.contains(valueAfterL)) {
          queue.add(new Node(valueAfterL, curr.getHistory()+"L"));
          visited.add(valueAfterL);
        }
        int valueAfterR = doCommand(curr.getValue(), 'R');
        if (!visited.contains(valueAfterR)) {
          queue.add(new Node(valueAfterR, curr.getHistory()+"R"));
          visited.add(valueAfterR);
        }
      }
    }
  }

  private static int doCommand(int value, char command) {
    switch (command) {
      case 'D':
        return (value * 2) % 10000;
      case 'S':
        return (value == 0) ? 9999 : value - 1;
      case 'L':
        return (value % 1000) * 10 + (value / 1000);
      case 'R':
        return (value % 10) * 1000 + (value / 10);
      default:
        return 0;
    }
  }
}