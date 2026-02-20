import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    Map<String, Integer> nameToNumber = new HashMap<>();
    String[] numberToName = new String[N+1];

    for (int i = 1; i <= N; i++) {
      String name = br.readLine();
      nameToNumber.put(name, i);
      numberToName[i] = name;
    }

    for (int i=0; i < M; i++) {
      String input = br.readLine();
      if (nameToNumber.containsKey(input)) {
        System.out.println(nameToNumber.get(input));
      } else {
        System.out.println(numberToName[Integer.parseInt(input)]);
      }
    }
  }
}
