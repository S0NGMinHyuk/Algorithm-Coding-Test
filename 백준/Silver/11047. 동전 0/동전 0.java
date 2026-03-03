import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringBuilder sb = new StringBuilder();
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int balance = Integer.parseInt(st.nextToken());
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    while (n-- > 0) {
      pq.add(Integer.parseInt(br.readLine()));
    }

    int result = 0;
    while (!pq.isEmpty()) {
      int coin = pq.poll();
      result += balance / coin;
      balance %= coin;
    }

    System.out.println(result);
  }
}