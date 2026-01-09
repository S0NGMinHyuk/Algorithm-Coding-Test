import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

  static StringBuilder sb = new StringBuilder();
  static List<Integer> list;
  static int[] visited;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    // N, M 값 저장
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    visited = new int[N];
    list = new ArrayList<>();

    // N개의 수 저장
    for (int i = 0; i < N; i++) {
      list.add(Integer.parseInt(st.nextToken()));
    }
    Collections.sort(list); // 미리 자연수를 오름차순으로 정렬
    dfs(M);
  }

  public static void dfs(int limit) {
    if (limit == 0) {
      System.out.println(sb.toString());
      return;
    }
    int prev = 0; // 수열 중복값 방지용 변수
    for (int i = 0; i < list.size(); i++) {
      if (visited[i] == 0 && list.get(i) != prev) {
        int before = sb.length();
        prev = list.get(i); // 현재 값 저장
        visited[i] = 1;
        sb.append(list.get(i)).append(" ");
        dfs(limit-1);
        visited[i] = 0; // sb 값을 이전으로 되돌리기
        sb.delete(before, sb.length());
      }
    }
  }
}
