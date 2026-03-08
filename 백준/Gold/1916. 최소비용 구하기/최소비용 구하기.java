import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    int towns = Integer.parseInt(br.readLine());
    int buses = Integer.parseInt(br.readLine());

    int[][] graph = new int[towns+1][towns+1];
    for (int i = 1; i <= towns; i++) {
      Arrays.fill(graph[i], -1);
    }

    for (int i = 0; i < buses; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      if (graph[from][to] == -1) {
        graph[from][to] = weight;
      } else {
        graph[from][to] = Math.min(graph[from][to], weight);
      }
    }
    StringTokenizer st = new StringTokenizer(br.readLine());
    int from = Integer.parseInt(st.nextToken());
    int to = Integer.parseInt(st.nextToken());

    long[] distance = new long[towns+1];
    Arrays.fill(distance, Long.MAX_VALUE);
    distance[from] = 0;

    Queue<Integer> q = new LinkedList<>();
    q.offer(from);

    while (!q.isEmpty()) {
      int curr = q.poll();
      for (int next=1; next<=towns; next++) {
        int weight = graph[curr][next];
        if (weight == -1) continue;
        else if (distance[next] > distance[curr] + weight) {
          distance[next] = distance[curr] + weight;
          q.offer(next);
        }
      }
    }

    System.out.println(distance[to]);
  }
}