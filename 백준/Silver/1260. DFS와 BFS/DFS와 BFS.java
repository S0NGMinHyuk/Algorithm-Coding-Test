import java.io.*;
import java.util.*;

public class Main {

  public static Set<Integer> visited;
  public static Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int start = Integer.parseInt(st.nextToken());

    for (int i=1; i<=N; i++) {
      map.put(i, new PriorityQueue<>());
    }
    
    // 그래프 생성
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      map.get(a).offer(b);
      map.get(b).offer(a);
    }

    // DFS 실행
    visited = new HashSet<>();
    dfs(start);
    sb.append("\n");

    // BFS 실행
    visited = new HashSet<>();
    bfs(start);

    System.out.println(sb.toString());
  }

  public static void dfs(int curr) {
    PriorityQueue<Integer> rollback = new PriorityQueue<>();
    sb.append(curr).append(" ");
    visited.add(curr);
    PriorityQueue<Integer> children = map.get(curr);
    while (!children.isEmpty()) {
      int child = children.poll();
      if (!visited.contains(child)) {
        dfs(child);
      }
      rollback.add(child);
    }
    map.put(curr, rollback);
  }

  public static void bfs(int curr) {
    Queue<Integer> queue = new ArrayDeque<>();
    queue.add(curr);

    while (!queue.isEmpty()) {
      int n = queue.poll();
      sb.append(n).append(" ");
      visited.add(curr);
      PriorityQueue<Integer> children = map.get(n);
      while (!children.isEmpty()) {
        int child = children.poll();
        if (!visited.contains(child)) {
          queue.offer(child);
          visited.add(child);
        }
      }
    }
  }
}
