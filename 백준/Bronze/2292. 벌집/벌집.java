import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());

    int layer = 0;
    int number = 1;

    if (n == 1) {
      System.out.println(1);
      return;
    }

    while (number < n) {
      number += 6 * layer++;
    }
    System.out.println(layer);
  }
}
