import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int goal = Integer.parseInt(st.nextToken());
    int answer = 0;

    for (int i=1; i<=goal; i++) {
      int result = i;
      int num = i;
      while (num > 0) {
        result += num % 10;
        num /= 10;
      }
      if (result == goal) {
        answer = i;
        break;
      }
    }
    System.out.println(answer);
  }
}
