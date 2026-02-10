import java.io.*;
import java.util.*;

public class Main {

  public static ArrayList<Integer> arr = new ArrayList<>();
  public static int N;
  public static int result = 0;

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < K; i++) {
      arr.add(Integer.parseInt(st.nextToken()));
    }

    dfs(0);
    System.out.println(result);
  }

  public static void dfs(int prev) {
    if (prev > N) {
      return;
    } else {
      result = Math.max(result, prev);
    }

    for (int n : arr) {
      dfs(prev*10 + n);
    }
  }
}
