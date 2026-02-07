import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    int target = 0;
    for (int i=0; i<3; i++) {
      String line = br.readLine();
      if (!line.equals("Fizz") && !line.equals("Buzz") && !line.equals("FizzBuzz")) {
        target = Integer.parseInt(line) + (3-i);
      }
    }

    String result = String.valueOf(target);
    if (target % 3 == 0) {
      if (target % 5 == 0) {
        result = "FizzBuzz";
      } else {
        result = "Fizz";
      }
    } else if (target % 5 == 0) {
      result = "Buzz";
    }
    System.out.println(result);
  }
}
