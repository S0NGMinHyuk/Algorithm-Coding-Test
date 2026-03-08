import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken()); // 사다리
    int M = Integer.parseInt(st.nextToken()); // 뱀

    // 사다리와 뱀 정보를 하나의 배열에 저장 (1~100)
    int[] move = new int[101];
    for (int i = 1; i <= 100; i++) move[i] = i;

    for (int i = 0; i < N + M; i++) {
      st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      move[from] = to;
    }

    System.out.println(bfs(move));
  }

  private static int bfs(int[] move) {
    Queue<Integer> queue = new LinkedList<>();
    int[] dist = new int[101]; // 방문 여부 및 주사위 횟수 저장
    Arrays.fill(dist, -1);

    queue.offer(1); // 1번 칸에서 시작
    dist[1] = 0;

    while (!queue.isEmpty()) {
      int curr = queue.poll();

      if (curr == 100) return dist[curr];

      for (int i = 1; i <= 6; i++) {
        int next = curr + i;

        if (next > 100) continue; // 100번을 넘어가면 무시

        // 사다리나 뱀이 있다면 그 목적지로 이동, 없다면 그대로 next
        int finalDest = move[next];

        if (dist[finalDest] == -1) { // 아직 방문하지 않은 칸이라면
          dist[finalDest] = dist[curr] + 1;
          queue.offer(finalDest);
        }
      }
    }
    return -1;
  }
}