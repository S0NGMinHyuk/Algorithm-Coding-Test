import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int up = Integer.parseInt(st.nextToken());
    int down = Integer.parseInt(st.nextToken());
    int distance =  Integer.parseInt(st.nextToken());

    distance -= up;
    int days = (distance / (up - down));
    if (distance % (up - down) != 0) {
      days++;
    }

    System.out.println(1 + days);
  }
}
