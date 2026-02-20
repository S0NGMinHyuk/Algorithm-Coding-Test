import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    List<Integer> list = new ArrayList<>();
    String input = br.readLine();
    String[] nums = input.split("\\-");
    for (String num : nums) {
      String[] temp = num.split("\\+");
      int value = 0;
      for (String s : temp) {
        value += Integer.parseInt(s);
      }
      list.add(value);
    }

    int answer = list.get(0);
    for (int i=1; i<list.size(); i++) {
      answer -= list.get(i);
    }
    System.out.println(answer);
  }
}
