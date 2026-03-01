import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine());
    List<Integer> list = new ArrayList<>();
    int maxValue = 3;

    while (T-- > 0) {
      int v = Integer.parseInt(br.readLine());
      list.add(v);
      maxValue = Math.max(maxValue, v);
    }

    long[] dp = new long[maxValue + 1];
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    int index = 4;
    while (index <= maxValue) {
      dp[index] = dp[index - 2] + dp[index - 3];
      index++;
    }

    for (int i=0; i<list.size(); i++) {
      sb.append(dp[list.get(i)]).append('\n');
    }
    System.out.println(sb);
  }
}