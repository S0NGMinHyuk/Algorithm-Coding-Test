#include <iostream>
#include <vector>
#include <queue>

#define MAX 1001

using namespace std;

int main()
{
    int graph[MAX][MAX] = {0,};
    int n, m, x;
    cin >> n >> m >> x;

    // 그래프 내용 입력
    for(int i=0; i<m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a][b] = w;
    }

    // x 마을에서 각자 마을까지의 거리 구하기
    queue<int> q;
    vector<int> x_to_n(n+1);
    q.push(x);
    while(!q.empty()) {
        int now = q.front();
        q.pop();
        for(int i=1; i<n+1; i++) {
            if(i != x && graph[now][i] > 0 && (x_to_n[i] == 0 || x_to_n[i] > x_to_n[now] + graph[now][i])) {
                q.push(i);
                x_to_n[i] = x_to_n[now] + graph[now][i];
            }
        }
    }

    // 각자 마을에서 x마을까지의 거리 구하기
    vector<int> n_to_x(n+1);
    q.push(x);
    while(!q.empty()) {
        int now = q.front();
        q.pop();
        for(int i=1; i<n+1; i++) {
            if(i != x && graph[i][now] > 0 && (n_to_x[i] == 0 || n_to_x[i] > n_to_x[now] + graph[i][now])) {
                q.push(i);
                n_to_x[i] = n_to_x[now] + graph[i][now];
            }
        }
    }

    // 왕복 길이가 가장 긴 마을 거리 구하기
    int result = 0;
    for(int i=1; i<n+1; i++) {
        result = max(result, n_to_x[i] + x_to_n[i]);
    }

    cout << result;
}