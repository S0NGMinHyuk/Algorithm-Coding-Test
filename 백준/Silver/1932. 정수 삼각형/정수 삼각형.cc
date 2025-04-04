#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 트리 입력받기
    int loop, n;
    cin >> loop;
    vector<vector<int>> graph;

    for(int i=0; i<loop; i++) {
        vector<int> temp;
        for(int j=0; j<i+1; j++) {
            cin >> n;
            temp.push_back(n);
        }
        graph.push_back(temp);
    }

    // leaf에서 root로 가는 최대경로 찾기
    for(int i=loop-2; i>=0; i--) {
        for(int j=0; j<graph[i].size(); j++) {
            graph[i][j] += max(graph[i+1][j], graph[i+1][j+1]);
        }
    }

    cout << graph[0][0];
}