import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    List<Integer> list = new ArrayList<>();
    int N = Integer.parseInt(br.readLine());
    for (int i = 0; i < N; i++) {
      list.add(Integer.parseInt(br.readLine()));
    }
    Collections.sort(list);

    int padding = (int) Math.round(N * 0.15);
    float sum = 0;
    for (int i=padding; i<list.size()-padding; i++) {
      sum += list.get(i);
    }

    System.out.println(Math.round(sum / (list.size() - (padding*2))));
  }
}
