import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());

    while (T-- > 0) {
      String command = br.readLine();
      int n = Integer.parseInt(br.readLine());
      String arrStr = br.readLine();

      // 1. Deque를 사용하여 양방향 제거가 가능하도록 설정
      Deque<Integer> deque = new ArrayDeque<>();
      StringTokenizer st = new StringTokenizer(arrStr, "[],");
      for (int i = 0; i < n; i++) {
        deque.add(Integer.parseInt(st.nextToken()));
      }

      boolean isReversed = false;
      boolean isError = false;

      for (char cmd : command.toCharArray()) {
        if (cmd == 'R') {
          isReversed = !isReversed;
        } else {
          // 2. D 연산 시 비어있으면 에러
          if (deque.isEmpty()) {
            isError = true;
            break;
          }
          if (isReversed) {
            deque.pollLast();
          } else {
            deque.pollFirst();
          }
        }
      }

      // 3. 출력 형식 맞추기
      if (isError) {
        sb.append("error\n");
      } else {
        makeString(deque, isReversed, sb);
      }
    }
    System.out.print(sb);
  }

  private static void makeString(Deque<Integer> deque, boolean isReversed, StringBuilder sb) {
    sb.append("[");
    while (!deque.isEmpty()) {
      sb.append(isReversed ? deque.pollLast() : deque.pollFirst());
      if (!deque.isEmpty()) sb.append(",");
    }
    sb.append("]\n");
  }
}
