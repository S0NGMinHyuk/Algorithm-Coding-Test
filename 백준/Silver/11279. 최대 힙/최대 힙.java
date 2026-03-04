import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringBuilder sb = new StringBuilder();
    StringBuilder sb = new StringBuilder();
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    int T = Integer.parseInt(br.readLine());
    while (T-- > 0) {
      int n = Integer.parseInt(br.readLine());
      if (n != 0) {
        pq.add(n);
      } else {
        if (pq.isEmpty()) {
          sb.append(0);
        } else {
          sb.append(pq.poll());
        }
        sb.append('\n');
      }
    }
    System.out.println(sb);
  }
}