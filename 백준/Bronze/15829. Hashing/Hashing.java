import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    String key = br.readLine();

    long r = 1L;
    long M = 1234567891;
    long result = 0;

    for (int i=0; i<N; i++) {
      int value = key.charAt(i) - 'a' + 1;
      result += value * r % M;
      r *= 31;
      r %= M;
    }
    System.out.println(result % M);
  }
}
