import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    String key = br.readLine();

    long r = 1L;
    int M = 1234567891;
    int result = 0;

    for (int i=0; i<N; i++) {
      int value = key.charAt(i) - 'a' + 1;
      result += value * r % M;
      r *= 31;
    }
    System.out.println(result);
  }
}
