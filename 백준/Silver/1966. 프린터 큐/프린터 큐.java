import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int rotate = Integer.parseInt(st.nextToken());
    for (int a=0; a<rotate; a++) {    // 문제 케이스만큼 반복
      st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());        // 프린트할 문서 개수
      int target = Integer.parseInt(st.nextToken());   // 출력 순서를 알고싶은 문서 위치

      Queue<Integer> queue = new ArrayDeque<>();
      PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

      st = new StringTokenizer(br.readLine());
      for (int i=0; i<n; i++) {    // 큐와 힙에 문서 추가
        int next  = Integer.parseInt(st.nextToken());
        queue.add(next);
        heap.add(next);
      }

      int count = 1;
      while (!queue.isEmpty()) {
        int curr = queue.poll();
        if (curr == heap.peek()) {  // 맨 앞에 있는 문서가 중요도가 가장 높은 문서인 경우
          heap.poll();
          if (target == 0) {        // 출력 순서가 궁금했던 파일인 경우
            System.out.println(count);
            break;
          } else {
            count++;    // 출력 순서 1 증가
          }
        } else {    // 중요도가 가장 높은 문서가 아니면 다시 큐에 추가
          queue.add(curr);
        }

        if (target == 0) {    // 순서가 궁금한 문서의 현위치 갱신
          target = queue.size()-1;
        } else {
          target--;
        }
      }
    }
  }
}
