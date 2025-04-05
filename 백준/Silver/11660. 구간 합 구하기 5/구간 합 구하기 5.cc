#include <iostream>
#include <vector>
#include <queue>

#define MAX 10000

using namespace std;

int main()
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    vector<vector<long long>> graph;
    int n, l;
    cin >> n >> l;

    // 그래프 입력
    for(int i=0; i<n+1; i++) {
        vector<long long> temp(n+1);
        if(i > 0) {
            for(int j=1; j<n+1; j++) {
                cin >> temp[j];
            }
        }
        graph.push_back(temp);
    }

    // 그래프 합 구하기
    for(int i=1; i<n+1; i++) {
        for(int j=1; j<n+1; j++) {
            graph[i][j] += graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1];
        }
    }

    // 그래프 값 출력
    int x1, x2, y1, y2;
    for(int i=0; i<l; i++) {
        cin >> x1 >> x2 >> y1 >> y2;
        x1--; x2--;
        cout << graph[y1][y2] + graph[x1][x2] - graph[y1][x2] - graph[x1][y2] << '\n';
    }
}