import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = 1;
        List<Set<Integer>> data = new ArrayList<>();
        data.add(new HashSet<>());
        
        while (answer < 9) {
            // N answer개로 만들 수 있는 집합 추가 by DP
            Set<Integer> numbers = new HashSet<>();
            numbers.add(makeFives(answer, N));
            for (int i=1; i<answer; i++) {
                numbers.addAll(makeNumbers(data.get(i), data.get(answer-i)));
            }
            if (numbers.contains(number)) {
                return answer;
            }
            data.add(numbers);
            answer++;
        }
        return -1;
    }
    
    public Set<Integer> makeNumbers(Set<Integer> lst1, Set<Integer> lst2) {
        Set<Integer> results = new HashSet<>();
        for (int a : lst1) {
            for (int b : lst2) {
                results.add(a+b);
                results.add(a-b);
                results.add(a*b);
                if (b != 0)
                    results.add(a/b);
            }
        }
        return results;
    }

    public int makeFives(int length, int N) {
        int result = 0;
        while (length > 0) {
            result *= 10;
            result += N;
            length--;
        }
        return result;
    }
}