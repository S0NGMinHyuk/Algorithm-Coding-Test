import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int answer = 0;
    Queue<Integer> queue = new LinkedList<>();
    Map<Integer, Integer> map = new HashMap<>();

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      int next = Integer.parseInt(st.nextToken());
      while (map.size() >= 2 && !map.containsKey(next)) { 
        // 세번째 과일이 들어온 경우, 현재 막대기의 과일 종류를 하나만 남기기
        int prev = queue.poll();
        int amount = map.get(prev) - 1;
        if (amount == 0) {
          map.remove(prev);
          // 해당 종류의 마지막 과일인 경우, key 삭제
        } else {
          map.put(prev, amount);
        }
      }
      map.putIfAbsent(next, 0);
      map.put(next, map.get(next) + 1);
      queue.add(next);
      answer = Math.max(queue.size(), answer);
      // 큐(막대)에 있는 최대 과일 수 갱신
    }
    System.out.println(answer);
  }
}