import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

    while (T--> 0) {
      int k = Integer.parseInt(br.readLine()); // 연산 개수
      TreeMap<Integer, Integer> map = new TreeMap<>();

      for (int i = 0; i < k; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        char cmd = st.nextToken().charAt(0);
        int value = Integer.parseInt(st.nextToken());

        if (cmd == 'I') {
          // 삽입: 값이 있으면 개수 +1, 없으면 1
          map.put(value, map.getOrDefault(value, 0) + 1);
        } else {
          // 삭제: 맵이 비어있으면 무시
          if (map.isEmpty()) continue;

          // value가 1이면 최댓값, -1이면 최솟값의 키를 가져옴
          int key = (value == 1) ? map.lastKey() : map.firstKey();

          // 개수가 1개면 아예 삭제, 여러 개면 개수만 줄임
          if (map.get(key) == 1) {
            map.remove(key);
          } else {
            map.put(key, map.get(key) - 1);
          }
        }
      }

      if (map.isEmpty()) {
        System.out.println("EMPTY");
      } else {
        System.out.println(map.lastKey() + " " + map.firstKey());
      }
    }
  }
}