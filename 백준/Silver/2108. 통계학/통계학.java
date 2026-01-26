import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    long total = 0;
    int min = 4000;
    int max = -4000;
    int frequency = 0;
    List<Integer> frequencyList = new ArrayList<>();
    HashMap<Integer, Integer> map = new HashMap<>();
    List<Integer> list = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      int num = Integer.parseInt(st.nextToken());

      total += num;
      min = Math.min(min, num);
      max = Math.max(max, num);
      list.add(num);
      
      map.putIfAbsent(num, 0);
      map.put(num, map.get(num) + 1);
      if (map.get(num) > frequency) {
        frequency = map.get(num);
        frequencyList = new ArrayList<>(List.of(num));
      } else if (map.get(num) == frequency) {
        frequencyList.add(num);
      }
    }
    Collections.sort(list);

    // 출력 담당
    System.out.println(Math.round((float) total/N));  // 산술평균
    System.out.println(list.get(N/2));                // 중앙값
    if (frequencyList.size() == 1) {                  // 최빈값
      System.out.println(frequencyList.get(0));
    } else {
      Collections.sort(frequencyList);
      System.out.println(frequencyList.get(1));
    }
    System.out.println(max-min);                      // 범위
  }
}
