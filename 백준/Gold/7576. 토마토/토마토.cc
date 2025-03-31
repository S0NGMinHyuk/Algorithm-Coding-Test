#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() 
{
    int c, r, tomatoes = 0;
    cin >> c >> r;

    queue<pair<int, int>> q;
    vector<vector<int>> graph;
    for(int i=0; i<r; i++) {
        vector<int> temp;
        for(int j=0; j<c; j++) {
            int input;
            cin >> input;
            if(input == 1) {
                q.push(make_pair(i, j));
            }
            else if (input == 0) {
                tomatoes++; // 안익은 토마토 개수 증가
            }
            temp.push_back(input);
        }
        graph.push_back(temp);
    }

    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    int days = 0;
    while(!q.empty()){  // BFS로 탐색
        pair<int, int> rc = q.front();
        q.pop();
        days = max(days, graph[rc.first][rc.second]);   // 필요한 날짜 수 갱신

        for(int i=0; i<4; i++) {    // 상하좌우 탐색
            int nx = rc.first + dx[i];
            int ny = rc.second + dy[i];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c && graph[nx][ny] == 0) {
                graph[nx][ny] = graph[rc.first][rc.second] + 1;
                q.push(make_pair(nx, ny));
                tomatoes--; // 토마토가 익으면 남은 토마토 개수 1 감소
            }
        }
    }   

    if(tomatoes == 0) cout << days-1;   // 모든 토마토가 익은 경우
    else cout << -1;                    // 모든 토마토가 익지 않은 경우
}