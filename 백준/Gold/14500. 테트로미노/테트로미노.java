
import java.io.*;
import java.util.*;


public class Main {

  static int[][] graph;
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringBuilder sb = new StringBuilder();
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    graph = new int[n][m];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        graph[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int maxValue = 0;
    for (int i=0; i<n; i++) {
      for (int j=0; j<m; j++) {
        maxValue = Math.max(maxValue, getMaxTetromino(n, m, i, j));
      }
    }
    System.out.println(maxValue);
  }

  public static int getMaxTetromino(int n, int m, int i, int j) {
    int[][][] shapes = {
            {{0,1},{0,2},{0,3}}, // ㅡ
            {{1,0},{2,0},{3,0}}, // ㅣ

            {{0,1},{1,1},{1,0}}, // ㅁ

            {{0,-1},{0,1},{1,0}},  // ㅜ
            {{0,-1},{0,1},{-1,0}}, // ㅗ
            {{0,1},{-1,0},{1,0}},  // ㅏ
            {{0,-1},{-1,0},{1,0}}, // ㅓ

            {{1,0},{1,1},{2,1}},
            {{0,1},{-1,1},{-1,2}},
            {{1,0},{1,-1},{2,-1}},
            {{0,1},{1,1},{1,2}},

            {{0,1},{0,2},{1,2}},
            {{0,1},{0,2},{-1,2}},
            {{1,0},{2,0},{2,1}},
            {{1,0},{2,0},{2,-1}},
            {{0,-1},{0,-2},{1,-2}},
            {{0,-1},{0,-2},{-1,-2}},
            {{-1,0},{-2,0},{-2,1}},
            {{-1,0},{-2,0},{-2,-1}},
    };

    int result = 0;
    for (int[][] shape : shapes) {
      int[] a = {i, j};
      int[] b = {i+shape[0][0], j+shape[0][1]};
      int[] c = {i+shape[1][0], j+shape[1][1]};
      int[] d = {i+shape[2][0], j+shape[2][1]};

      if (!(0 <= b[0] && b[0] < n && 0 <= b[1] && b[1] < m)) {continue;}
      if (!(0 <= c[0] && c[0] < n && 0 <= c[1] && c[1] < m)) {continue;}
      if (!(0 <= d[0] && d[0] < n && 0 <= d[1] && d[1] < m)) {continue;}
      result = Math.max(result, graph[a[0]][a[1]]+graph[b[0]][b[1]]+graph[c[0]][c[1]]+graph[d[0]][d[1]]);
    }
    return result;
  }


}