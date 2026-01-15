import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 전체 노드 개수
    int N = Integer.parseInt(st.nextToken());

    // 전체 버스 개수
    st = new StringTokenizer(br.readLine());
    int M = Integer.parseInt(st.nextToken());

    int[][] graph = new int[N+1][N+1];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        graph[i][j] = 1000000000;
      }
      graph[i][i] = 0;
    }

    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int weight = Integer.parseInt(st.nextToken());
      graph[from][to] = Math.min(graph[from][to], weight);
    }

    for (int k = 1; k <= N; k++) {
      for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
          if (graph[i][k] + graph[k][j] < graph[i][j]) {
            graph[i][j] = graph[i][k] + graph[k][j];
          }
        }
      }
    }
    for (int i=1; i<=N; i++) {
      for (int j=1; j<=N; j++) {
        if (graph[i][j] == 1000000000)
          System.out.print(0 + " ");
        else
          System.out.print(graph[i][j] + " ");
      }
      System.out.println();
    }
  }
}
