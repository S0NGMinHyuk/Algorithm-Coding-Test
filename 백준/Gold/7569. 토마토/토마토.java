import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int M = Integer.parseInt(st.nextToken());
    int N = Integer.parseInt(st.nextToken());
    int H = Integer.parseInt(st.nextToken());

    int[][][] box = new int[H][N][M];
    Queue<int[]> queue = new ArrayDeque<>();
    int rare = 0;
    for (int h = 0; h < H; h++) {
      for (int n = 0; n < N; n++) {
        st = new StringTokenizer(br.readLine());
        for (int m = 0; m < M; m++) {
          box[h][n][m] = Integer.parseInt(st.nextToken());
          if (box[h][n][m] == 1) {
            queue.add(new int[]{h, n, m, 0});
          } else if (box[h][n][m] == 0) {
            rare++;
          }
        }
      }
    }

    int dates = 0;
    int[] dx = {-1, 1, 0, 0, 0, 0};
    int[] dy = {0, 0, -1, 1, 0, 0};
    int[] dh = {0, 0, 0, 0, 1, -1};
    while (!queue.isEmpty()) {
      int[] curr = queue.poll();
      dates = Math.max(dates, curr[3]);
      for (int i=0; i<6; i++) {
        int nh = curr[0]+dh[i];
        int nx = curr[1]+dx[i];
        int nw = curr[2]+dy[i];
        if (0 <= nh && nh < H && 0 <= nx && nx < N && 0 <= nw && nw < M) {
          if (box[nh][nx][nw] == 0) {
            queue.add(new int[]{nh, nx, nw, curr[3]+1});
            box[nh][nx][nw] = 1;
            rare--;
          }
        }
      }
    }
    if (rare == 0) {
      System.out.println(dates);
    } else {
      System.out.println(-1);
    }
  }
}
