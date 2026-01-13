import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // 전체 노드 개수
    int nodeAmount = Integer.parseInt(st.nextToken());
    Map<Integer, List<Integer>> map = new HashMap<>();

    for (int i=0; i<nodeAmount-1; i++) {
      st = new StringTokenizer(br.readLine());  // 한줄 한줄 읽기
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      map.putIfAbsent(a, new ArrayList<>());    // value List가 비어있으면 채우기
      map.putIfAbsent(b, new ArrayList<>());
      map.get(a).add(b);
      map.get(b).add(a);
    }
  
    int[] parents = new int[nodeAmount+1];      // -1로 초기화
    Arrays.fill(parents, -1);

    Queue<Integer> queue = new LinkedList<>();  // 1번 노드부터 실행
    queue.add(1);
    parents[1] = 0;

    while (!queue.isEmpty()) {
      int curr = queue.poll();
      for (int child : map.get(curr)) {
        if (parents[child] == -1) {             // curr 노드가 부모노드인 노드
          parents[child] = curr;
          queue.add(child);
        }
      }
    }

    for (int i=2; i<=nodeAmount; i++) {         // 정답 출력
      System.out.println(parents[i]);
    }
  }
}
