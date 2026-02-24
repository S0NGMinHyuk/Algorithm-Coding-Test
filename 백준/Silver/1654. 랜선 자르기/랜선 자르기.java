import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int cableAmount = Integer.parseInt(st.nextToken());
    int required = Integer.parseInt(st.nextToken());

    List<Integer> cables = new ArrayList<>();
    for (int i=0; i<cableAmount; i++){
      cables.add(Integer.parseInt(br.readLine()));
    }

    long left = 1L;
    long right = Integer.MAX_VALUE;
    long answer = 0L;
    while (left <= right) {
      long mid = (left+right)/2;
      long amount = 0;
      for (int cable : cables){
        amount += cable/mid;
      }
      if (amount >= required) {
        // mid 길이를 N개 이상 만들 수 있는 경우
        answer = mid;
        left = mid+1;
      } else {
        // mid 길이를 N개 이상 만들 수 없는 경우
        right = mid-1;
      }
    }
    System.out.println(answer);
  }
}
