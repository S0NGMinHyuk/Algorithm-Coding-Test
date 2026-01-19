import java.io.*;
import java.util.*;

public class Main {

  public static List<Integer> list = new ArrayList<>();
  public static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int start = Integer.parseInt(st.nextToken());
    int end = Integer.parseInt(st.nextToken());
    
    int[] arr = new int[end+1];
    for (int i=start; i<=end; i++) {
      arr[i] = i;
    }
    arr[1] = 0;  // 1은 소수가 아니다.

    for (int i=2; i<=Math.sqrt(end)+1; i++) {
      int index = i*2;
      while (index <= end) {
        arr[index] = 0;
        index += i;
      }
    }

    for (int i=start; i<=end; i++) {
      if (arr[i] != 0) {
        System.out.println(i);
      }
    }
  }
}
