#include <iostream>
#include <queue>

#define MAX 101

using namespace std;

int main()

{
    int graph[MAX][MAX] = {0,};
    int temp, loop;
    cin >> temp;
    cin >> loop;
    
    // 입력값에 따라 그래프 생성
    for (int i=0; i<loop; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    // 1번 컴퓨터부터 연결된 컴퓨터 개수를 BFS 알고리즘으로 탐색
    int visited[MAX] = {0,};
    int count = 0;
    queue<int> q;

    // 기본값으로 1 추가
    q.push(1);
    visited[1] = 1;

    while(!q.empty()) { // BFS 알고리즘
        int com = q.front();
        q.pop();

        for(int i=0; i<MAX; i++) {
            if (graph[com][i] == 1 && visited[i] == 0) {
                q.push(i);
                visited[i] = 1;
                count++;
            }
        }
    }

    cout << count;
}