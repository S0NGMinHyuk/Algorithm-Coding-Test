import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());
//    StringBuilder sb = new StringBuilder();

    String isbn = br.readLine();
    boolean isOdd = true;
    int sum = 0;

    for (int i=1; i<=isbn.length(); i++) {
      String ch = isbn.charAt(i-1) + "";
      try {
        int n = Integer.parseInt(ch);
        if (i%2 == 0) {
          sum += n*3;
        } else {
          sum += n;
        }
      } catch (NumberFormatException e) {
        if (i%2 == 0) {
          isOdd = false;
        }
      }
    }

    int require = 10 - (sum % 10);
    if (require == 10) {
      System.out.println(0);
    } else if (isOdd) {
      System.out.println(require);
    } else {
      while (require % 3 !=  0) {
        require += 10;
      }
      System.out.println(require/3);
    }
  }
}
