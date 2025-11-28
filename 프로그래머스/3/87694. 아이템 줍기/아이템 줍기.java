// 사각형 테두리를 타야 할 땐
// 1. 사각형 가로세로를 2배로 증가
// 2. 사각형 내부는 1, 외부는 2로 저장. 나중에 2인 경우만 BFS 실행

import java.util.*;

class Solution {
    int[][] map = new int[101][101];
    
    public int solution(int[][] rectangle, int X, int Y, int itemX, int itemY) {
        for (int[] r: rectangle) 
            draw(r[0]*2, r[1]*2, r[2]*2, r[3]*2);
        
        int dx[]={0,0,-1,1};
        int dy[]={-1,1,0,0};
        
        boolean visited[][]=new boolean[101][101];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{Y*2, X*2, 0});    //  Y값, X값, 이동거리
        
        while(!queue.isEmpty()){
            int[] temp = queue.poll();
            int prevY = temp[0];
            int prevX = temp[1];
            int count = temp[2];
            
            if(prevY==itemY*2&&prevX==itemX*2)
                return count/2;
            
            for(int i=0;i<4;i++){   // 상하좌우 탐색
                int nextY = prevY+dy[i];
                int nextX = prevX+dx[i];
                if(nextY<0||nextX<0||nextY>=map.length||nextX>=map[0].length)
                    continue;   // 범위가 터지는 경우
                if(visited[nextY][nextX]==true||map[nextY][nextX] != 2)
                    continue;   // 이미 방문했거나 모서리가 아닌경우
                
                visited[nextY][nextX] = true;
                queue.add(new int[]{nextY, nextX, count+1});
              
            }
        }
        return 0;
    }
    
    public void draw(int x1,int y1,int x2,int y2){
        for(int i = y1; i <= y2; i++){
            for(int j = x1; j <= x2; j++){
            	if(map[i][j]==1) 
                    continue;  // 다른 도형의 내부인 경우
                map[i][j]=1;
                if(i==y1||i==y2||j==x1||j==x2) 
                    map[i][j]=2; // 모서리인 경우
            }
        }
        
    }
}