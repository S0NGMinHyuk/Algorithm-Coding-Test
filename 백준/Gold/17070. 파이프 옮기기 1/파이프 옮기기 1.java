import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    int EMPTY = 0;
    int WALL = 1;
    int n = Integer.parseInt(br.readLine());
    int[][] house = new int[n][n];
    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < n; j++) {
        house[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int HORIZON = 0;
    int VERTICAL = 1;
    int DIAGONAL = 2;
    int[][][] map = new int[n][n][3];
    map[0][1][HORIZON] = 1;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (house[i][j] == WALL) { continue; }
        else if (i == 0 && j <= 1) { continue; }

        // 가로로 배치될 수 있는 경우의 수
        if (j > 0) {
          map[i][j][HORIZON] = map[i][j-1][HORIZON] + map[i][j-1][DIAGONAL];
        }

        // 세로로 배치될 수 있는 경우의 수
        if (i > 0) {
          map[i][j][VERTICAL] = map[i-1][j][VERTICAL] + map[i-1][j][DIAGONAL];
        }

        // 대각으로 배치될 수 있는 경우의 수
        // 위쪽과 왼쪽 비어있는지 확인하기
        if (i > 0 && j > 0 && house[i-1][j] != WALL && house[i][j-1] != WALL) {
          map[i][j][DIAGONAL] = map[i-1][j-1][VERTICAL]
                                + map[i-1][j-1][HORIZON]
                                + map[i-1][j-1][DIAGONAL];
        }
      }
    }

    int result = map[n-1][n-1][HORIZON]
                  + map[n-1][n-1][VERTICAL]
                  + map[n-1][n-1][DIAGONAL];
    System.out.println(result);
  }
}