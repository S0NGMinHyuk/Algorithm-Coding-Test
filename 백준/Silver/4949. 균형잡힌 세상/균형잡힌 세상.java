import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    StringTokenizer st = new StringTokenizer(br.readLine());

    while (true) {
      Stack<Character> stack = new Stack<>();
      String line = br.readLine();
      if (line.equals(".")) {
        break;
      }

      for (int i=0; i<line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '(' || ch == '[') {
          stack.push(ch);
        } else if (ch == ')') {
          if (stack.isEmpty() || stack.peek() != '(') {
            System.out.println("no");
            break;
          } else {
            stack.pop();
          }
        } else if (ch == ']') {
          if (stack.isEmpty() || stack.peek() != '[') {
            System.out.println("no");
            break;
          } else {
            stack.pop();
          }
        } else if (ch == '.') {
          if (stack.isEmpty()) {
            System.out.println("yes");
          } else {
            System.out.println("no");
          }
          break;
        }
      }
    }
  }
}
