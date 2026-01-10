import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // N, M 값 저장
    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    int answer = 100001;
    int[] dp = new int[100001];
    Arrays.fill(dp, 100001);
    dp[N] = 0;

    Queue<Integer> q = new LinkedList<>();
    q.offer(N);
    while (!q.isEmpty()) {
      int curr = q.poll();
      if (curr == K) {
        answer = Math.min(answer, dp[curr]);
        continue;
      }

      // 순간이동 하는 경우
      if (curr * 2 <= K && dp[curr*2] > dp[curr]) {
        dp[curr*2] = dp[curr];
        q.offer(curr*2);
      } else if (curr*2 > K) {
        answer = Math.min(answer, curr*2 - K + dp[curr]);
      }
      // 앞으로 가는 경우
      if (curr+1 <= K && dp[curr+1] > dp[curr]+1) {
        dp[curr+1] = dp[curr]+1;
        q.offer(curr+1);
      }
      // 뒤로 가는 경우
      if (curr > 0 && dp[curr-1] > dp[curr]+1) {
        dp[curr-1] = dp[curr]+1;
        q.offer(curr-1);
      }
    }
    System.out.println(answer);
  }
}
