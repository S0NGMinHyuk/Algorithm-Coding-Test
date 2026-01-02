import java.util.*;

class Solution {
    public int solution(int[] a) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] lengths = new int[a.length+1];
        int answer = 0;
        
        for (int i=0; i<a.length; i++) {
            if (!map.containsKey(a[i])) {
                if (i > 0 && a[i] != a[i-1]) {  // 왼쪽 값을 갖는 경우
                    map.put(a[i], i);
                    lengths[a[i]] += 2;
                    answer = Math.max(answer, lengths[a[i]]);
                    continue;
                }
                if (i < a.length-1 && a[i] != a[i+1]) { // 오른쪽 값을 갖는 경우
                    map.put(a[i], i+1);
                    lengths[a[i]] += 2;
                    answer = Math.max(answer, lengths[a[i]]);
                    continue;
                }
                else {  // 어느것도 갖지 못하는 경우
                    map.put(a[i], i);
                }
            }
            else {
                int beforeIndex = map.get(a[i]);
                if (i > beforeIndex + 1) {  // 왼쪽 값을 갖는 경우
                    map.put(a[i], i);
                    lengths[a[i]] += 2;
                    answer = Math.max(answer, lengths[a[i]]);
                    continue;
                }
                if (i < a.length-1 && a[i] != a[i+1]) { // 오른쪽 값을 갖는 경우
                    map.put(a[i], i+1);
                    lengths[a[i]] += 2;
                    answer = Math.max(answer, lengths[a[i]]);
                    continue;
                }
                else {
                    map.put(a[i], i);
                }
            }
        }
        return answer;
    }
}