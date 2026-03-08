import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(br.readLine());

    List<Integer>[] graph = new List[N];
    for (int i = 0; i < N; i++) {
      graph[i] = new ArrayList<>();
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        if (st.nextToken().equals("1")) {
          graph[i].add(j);
        }
      }
    }

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < N; i++) {
      findPath(i, graph, sb);
    }
    System.out.println(sb);
  }

  private static void findPath(int src, List<Integer>[] graph, StringBuilder sb) {
    Queue<Integer> queue = new LinkedList<>();
    int[] visited = new int[graph.length];
    queue.add(src);

    while (!queue.isEmpty()) {
      int curr = queue.poll();
      for (int child : graph[curr]) {
        if (visited[child] == 0) {
          visited[child] = 1;
          queue.add(child);
        }
      }
    }

      for (int j : visited) {
          sb.append(j).append(" ");
      }
    sb.append("\n");
  }
}