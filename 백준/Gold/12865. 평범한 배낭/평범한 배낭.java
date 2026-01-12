import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // N, M 값 저장
    int stuffs = Integer.parseInt(st.nextToken());
    int limit = Integer.parseInt(st.nextToken());

    int[] prev =  new int[limit+1];
    int[] curr = new int[limit+1];

    for (int i = 0; i < stuffs; i++) {
      st = new StringTokenizer(br.readLine());
      int weight = Integer.parseInt(st.nextToken());
      int value = Integer.parseInt(st.nextToken());

      for (int j=weight; j<=limit; j++) {
        if (curr[j] < prev[j-weight] + value) { // 현재 물건을 담는 경우
          curr[j] = prev[j-weight] + value;
        }
      }
      prev = curr.clone();
    }
    System.out.println(curr[limit]);
  }
}
