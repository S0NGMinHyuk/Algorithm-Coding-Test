import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);

        int left = 1, right = distance;
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2; // 만들고 싶은 최소 거리
            int removed = 0;
            int prev = 0;

            for (int r : rocks) {
                if (r - prev < mid) {
                    removed++;          // 돌 제거
                } else {
                    prev = r;          // 돌 유지
                }
            }

            // 마지막(마지막 남긴 돌 ~ 도착지점) 구간 체크
            if (distance - prev < mid) removed++;

            if (removed > n) {          // 불가능 -> 최소거리 줄이기
                right = mid - 1;
            } else {                    // 가능 -> 더 키워보기
                answer = mid;
                left = mid + 1;
            }
        }

        return answer;
    }
}