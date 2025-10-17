import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while (n > 0) {
            answer += n % 10;
            n = (int) n / 10;
        }

        return answer;
    }
}