import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());
    StringBuilder sb = new StringBuilder();

    int N = Integer.parseInt(br.readLine());
    int[] result =  new int[N];

    for (int i = 0; i < N; i++) {
      result[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(result);
    for (int r : result) {
      sb.append(r).append("\n");
    }
    System.out.println(sb.toString());
  }
}
