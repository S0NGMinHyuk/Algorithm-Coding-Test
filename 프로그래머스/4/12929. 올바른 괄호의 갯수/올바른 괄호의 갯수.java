class Solution {
    public int solution(int n) {
        int[] arr = new int[15];
        arr[0] = 1;
        arr[1] = 1;
        
        for (int i=2; i<arr.length; i++) {
            for (int a = 0; a < i; a++) {
                int b = i-1-a;
                arr[i] += arr[a]*arr[b];
            }
        }
        
        return arr[n];
    }
}