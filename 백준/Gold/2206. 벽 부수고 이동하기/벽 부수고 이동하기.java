import java.io.*;
import java.util.*;

class Node {
  int x, y, count, broken; // broken: 0(안부심), 1(부심)

  public Node(int x, int y, int count, int broken) {
    this.x = x;
    this.y = y;
    this.count = count;
    this.broken = broken;
  }
}

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    int[][] graph = new int[N][M];
    for (int i = 0; i < N; i++) {
      String line = br.readLine();
      for (int j = 0; j < M; j++) {
        graph[i][j] = line.charAt(j) - '0';
      }
    }

    // 방문 체크: [x][y][벽파괴여부]
    // visited[x][y][0]: 벽을 하나도 안 부수고 (x,y)에 방문함
    // visited[x][y][1]: 벽을 하나 부수고 (x,y)에 방문함
    boolean[][][] visited = new boolean[N][M][2];

    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(0, 0, 1, 0));
    visited[0][0][0] = true;

    int[] dx = {0, 0, 1, -1};
    int[] dy = {1, -1, 0, 0};

    while (!queue.isEmpty()) {
      Node curr = queue.poll();

      if (curr.x == N - 1 && curr.y == M - 1) {
        System.out.println(curr.count);
        return;
      }

      for (int i = 0; i < 4; i++) {
        int nx = curr.x + dx[i];
        int ny = curr.y + dy[i];

        if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

        // 1. 이동할 곳이 빈 칸(0)인 경우
        if (graph[nx][ny] == 0) {
          if (!visited[nx][ny][curr.broken]) {
            visited[nx][ny][curr.broken] = true;
            queue.add(new Node(nx, ny, curr.count + 1, curr.broken));
          }
        }
        // 2. 이동할 곳이 벽(1)인 경우
        else if (graph[nx][ny] == 1) {
          // 아직 벽을 부순 적이 없다면 부수고 이동 가능
          if (curr.broken == 0 && !visited[nx][ny][1]) {
            visited[nx][ny][1] = true;
            queue.add(new Node(nx, ny, curr.count + 1, 1));
          }
        }
      }
    }
    System.out.println("-1");
  }
}