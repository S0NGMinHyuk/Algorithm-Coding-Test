import java.util.*;

class Solution {
    public int solution(int[] money) {
        // 첫 집을 훔치는 경우와 훔지지 않는 경우를 나눠서 최대값 구하기
        int a = steel(Arrays.copyOfRange(money, 0, money.length-1));
        int b = steel(Arrays.copyOfRange(money, 1, money.length));   
        return Math.max(a, b);
    }
    
    int steel(int[] money) {
        for (int i=2; i<money.length; i++) {
            if (i == 2)
                money[i] += money[0];
            else
                money[i] += Math.max(money[i-2], money[i-3]);
        }
        return Math.max(money[money.length-1], money[money.length-2]);
    }
}