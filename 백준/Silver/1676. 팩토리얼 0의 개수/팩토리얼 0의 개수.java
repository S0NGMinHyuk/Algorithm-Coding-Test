import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int answer = 0;
    for (int i=1; i<=N; i++) {
      int temp = i;
      while (temp%5 == 0) {
        answer++;
        temp /= 5;
      }
    }
    System.out.println(answer);
  }
}
