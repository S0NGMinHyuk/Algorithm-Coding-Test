import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    Map<Integer, List<Integer>> map = new HashMap<>();

    for (int i=1; i<=N; i++) {
      map.put(i, new ArrayList<>());
    }

    // 그래프 생성
    for (int i=0; i<M; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());

      map.get(x).add(y);
      map.get(y).add(x);
    }

    // 각 사람 별 케빈베이컨 지수 계산
    int index = N+1;
    int kevinBacon = Integer.MAX_VALUE;
    for (int i=1; i<=N; i++) {
      int myKevinBacon = 0;
      Queue<int[]> queue = new ArrayDeque<>();
      Set<Integer> visited = new HashSet<>();

      queue.add(new int[] {i, 0});
      visited.add(i);

      while (!queue.isEmpty()) {
        int[] curr = queue.poll();
        myKevinBacon += curr[1];
        for (int child : map.get(curr[0])) {
          if (!visited.contains(child)) {
            visited.add(child);
            queue.add(new int[] {child, curr[1]+1});
          }
        }
      }
      
      if (myKevinBacon < kevinBacon || (myKevinBacon == kevinBacon && i < index)) {
        kevinBacon = myKevinBacon;
        index = i;
      }
    }
    System.out.println(index);
  }
}
