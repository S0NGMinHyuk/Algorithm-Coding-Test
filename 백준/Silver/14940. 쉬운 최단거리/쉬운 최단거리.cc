#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    vector<vector<int>> graph;
    queue<pair<int, int>> q;
    int r, c;
    cin >> r >> c;

    // 지도 생성
    for(int i=0; i<r; i++) {
        vector<int> temp;
        for(int j=0; j<c; j++) {
            int n;
            cin >> n;
            if(n == 2) {
                temp.push_back(0);
                q.push(make_pair(i, j));
            }
            else if(n == 1) {
                temp.push_back(-1);
            }
            else if(n == 0) {
                temp.push_back(0);
            }
        }
        graph.push_back(temp);
    }

    // 목표지점까지의 거리 저장
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    while(!q.empty()) {
        pair<int, int> now = q.front();
        q.pop();

        for(int i=0; i<4; i++) {
            int nx = now.first + dx[i];
            int ny = now.second + dy[i];
            if(nx >= 0 && nx < r && ny >= 0 && ny < c && graph[nx][ny] == -1) {
                graph[nx][ny] = graph[now.first][now.second] + 1;
                q.push(make_pair(nx, ny));
            }
        }
    }

    // 답 출력
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            cout << graph[i][j] << ' ';
        }
        cout << '\n';
    }
}