import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int number = 1;

    for (int i=1; i<=N; i++) {
      st = new StringTokenizer(br.readLine());
      int curr = Integer.parseInt(st.nextToken());
      while (list.isEmpty() || list.get(list.size()-1) < curr) {
        list.add(number++);
        sb.append("+\n");
      }
      if (list.get(list.size()-1) == curr) {
        list.remove(list.size()-1);
        sb.append("-\n");
      } else {
        System.out.println("NO");
        return;
      }
    }
    System.out.println(sb.toString());
  }
}
