import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int[][] apart = new int[15][15];

    for (int i = 0; i < 15; i++) {
      apart[0][i] = i;
    }

    for (int i = 1; i < 15; i++) {
      int sum = 0;
      for (int j = 1; j < 15; j++) {
        sum += apart[i-1][j];
        apart[i][j] = sum;
      }
    }

    int n = Integer.parseInt(st.nextToken());
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      st = new StringTokenizer(br.readLine());
      int y = Integer.parseInt(st.nextToken());
      System.out.println(apart[x][y]);
    }

  }
}
