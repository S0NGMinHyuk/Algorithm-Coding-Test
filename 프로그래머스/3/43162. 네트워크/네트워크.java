class Solution {
    boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int i=0; i<n; i++) {
            if (visited[i] == false) {
                answer++;
                dfs(n, computers, i);
            }
        }
        
        return answer;
    }
    
    public void dfs(int n, int[][] computers, int index) {
        visited[index] = true;
        for (int i=0; i<n; i++) {
            if (computers[index][i] == 1 && visited[i] == false) {
                visited[i] = true;
                dfs(n, computers, i);
            }
        }
    }
}