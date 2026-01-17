import java.io.*;
import java.util.*;

public class Main {

  static Map<Character, Character[]> map = new HashMap<>();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int i = 666;
    while (true) {
      if (String.valueOf(i).contains("666")) {
        N--;
        if (N == 0) break;
      }
      i++;
    }
    System.out.println(i);
  }
}
