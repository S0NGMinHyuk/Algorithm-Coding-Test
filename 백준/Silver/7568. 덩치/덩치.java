import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int manCount = Integer.parseInt(st.nextToken());
    List<int[]> mans = new ArrayList<>();
    int[] result = new int[manCount];

    for (int i = 0; i < manCount; i++) {
      st = new StringTokenizer(br.readLine());
      int weight = Integer.parseInt(st.nextToken());
      int height = Integer.parseInt(st.nextToken());
      mans.add(new int[]{weight, height});
    }

    for (int i=0; i<manCount; i++) {
      int[] man = mans.get(i);
      int rank = 1;

      for (int j=0; j<manCount; j++) {
        int[] other = mans.get(j);
        if (other[0] > man[0] && other[1] > man[1]) {
          rank++;
        }
      }

      result[i] = rank;
    }

    for (int r : result) {
      System.out.print(r + " ");
    }
  }
}
