import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int length = Integer.parseInt(br.readLine());
    String input = br.readLine();

    int answer = 0;
    int index = 0;
    while (index+2 < length) {

        if (input.charAt(index) == 'I'
          && input.charAt(index+1) == 'O'
          && input.charAt(index+2) == 'I') {
          int repeat = 1;
          index += 3;
          while (true) {
            if (index+1 < length && input.charAt(index) == 'O' && input.charAt(index+1) == 'I') {
              repeat++;
              index += 2;
            } else { break; }
          }
          if (repeat >= n) {
            answer += repeat - n + 1;
          }
        } else {
          index++;
        }

    }
    System.out.println(answer);
  }
}
