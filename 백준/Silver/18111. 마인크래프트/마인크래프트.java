import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int inventory = Integer.parseInt(st.nextToken());

    int left = Integer.MAX_VALUE;
    int right = Integer.MIN_VALUE;
    Map<Integer, Integer> layer = new HashMap<>();
    for (int i=0; i<N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j=0; j<M; j++) {
        int l = Integer.parseInt(st.nextToken());
        layer.putIfAbsent(l, 0);
        layer.put(l, layer.get(l)+1);
        left = Math.min(left, l);
        right = Math.max(right, l);
      }
    }

    int[] answer = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE}; // [소요시간, 층]
    for (int mid = left; mid<=right; mid++) {
      int availableBlocks = inventory;
      int time = 0;
      for (int l : layer.keySet()) {
        if (l < mid) {
          availableBlocks -= layer.get(l) * (mid-l);  // mid 층으로 가기 위한 블록 설치
          time += layer.get(l) * (mid-l); // mid 층으로 가기 위한 블록 설치 시간
        } else if (l > mid) {
          availableBlocks += layer.get(l) * (l-mid);  // mid 층으로 가기 위한 블록 파괴
          time += layer.get(l) * (l-mid) * 2; // mid 층으로 가기 위한 블록 파괴 시간
        }
      }
      if (availableBlocks >= 0) {
        // mid 층으로 평탄화가 가능한 경우
        if (time < answer[0] || (time == answer[0] && mid > answer[1])) {
          answer[0] = time;
          answer[1] = mid;
        }
      } else {
        break;
      }
    }
    // 결과 출력
    System.out.println(answer[0] + " " + answer[1]);
  }
}
