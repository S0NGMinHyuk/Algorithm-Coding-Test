import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());
    while (T-- > 0) {
      int N = Integer.parseInt(br.readLine());
      Map<String, Integer> map = new HashMap<>();
      for (int i = 0; i < N; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        String cloth = st.nextToken();
        String tag = st.nextToken();
        map.putIfAbsent(tag, 1);
        map.put(tag, map.get(tag) + 1);
      }

      int answer = 1;
      for (String key : map.keySet()) {
        answer *= map.get(key);
      }
      sb.append(answer-1).append("\n");
    }
    System.out.println(sb);
  }
}