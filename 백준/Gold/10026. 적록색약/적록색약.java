import java.io.*;
import java.util.*;

public class Main {

  static final char RED = 'R';
  static final char BLUE = 'B';
  static final char GREEN = 'G';
  static int N;
  static int[] dx = new int[] {-1, 1, 0, 0};
  static int[] dy = new int[] {0, 0, -1, 1};

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringBuilder sb = new StringBuilder();

    N = Integer.parseInt(br.readLine());
    char[][] map1 = new char[N][N];
    char[][] map2 = new char[N][N];
    for (int i = 0; i < N; i++) {
      char[] input = br.readLine().toCharArray();
      for (int j = 0; j < N; j++) {
        map1[i][j] = input[j];
        map2[i][j] = input[j];
      }
    }

    int result1 = 0;
    int result2 = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (map1[i][j] != 'X') {
          String color1 = "";
          switch (map1[i][j]) {
            case RED:
              color1 = "R";
              break;
            case BLUE:
              color1 = "B";
              break;
            case GREEN:
              color1 = "G";
              break;
          }
          findArea(map1, i, j, color1);
          result1++;
        }
        if (map2[i][j] != 'X') {
          String color2 = "";
          switch (map2[i][j]) {
            case RED:
            case GREEN:
              color2 = "RG";
              break;
            case BLUE:
              color2 = "B";
              break;
          }
          findArea(map2, i, j, color2);
          result2++;
        }
      }
    }
    System.out.println(result1 +  " " + result2);
  }

  private static void findArea(char[][] map, int x, int y, String color) {
    Queue<int[]> queue = new LinkedList<>();
    Set<int[]> visited = new HashSet<>();

    queue.offer(new int[]{x,y});
    visited.add(new int[]{x,y});
    map[x][y] = 'X';
    while (!queue.isEmpty()) {
      int[] curr = queue.poll();
      for (int i = 0; i < 4; i++) {
        int nx = curr[0] + dx[i];
        int ny = curr[1] + dy[i];
        if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited.contains(new int[]{nx,ny})) {
          if (color.contains(java.lang.String.valueOf(map[nx][ny]))) {
            map[nx][ny] = 'X';
            queue.offer(new int[]{nx,ny});
          }
        }
      }
    }
  }
}