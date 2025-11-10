import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int food : scoville)  
            pq.add(food);
        
        while (pq.size() > 1 && pq.peek() < K) {
            answer++;
            int a = pq.poll();
            int b = pq.poll();
            pq.add(a+b+b);
        }
        
        if (pq.peek() < K)
            return -1;
        return answer;
    }
}