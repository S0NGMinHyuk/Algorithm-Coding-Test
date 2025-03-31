#include <iostream>
#include <vector>

using namespace std;

int blue = 0, white = 0;
vector<vector<int>> graph;

void dfs(int startX, int startY, int length);

int main()
{
    int length;
    cin >> length;
    for(int i=0; i<length; i++) {
        vector<int> temp;
        for(int i=0; i<length; i++) {
            int n;
            cin >> n;
            temp.push_back(n);
        }
        graph.push_back(temp);
    }

    dfs(0, 0, length);
    cout << white << '\n' << blue;
    return 0;
}

void dfs(int startX, int startY, int n) {
    int count = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            count += graph[startX+i][startY+j];
        }
    }

    if (count == n * n) blue++;     // 전체가 통일된 색인 경우
    else if (count == 0) white++;   // 전체가 통일된 색인 경우
    else {
        // 4등분해서 다시 재귀 호출
        dfs(startX, startY, n/2);
        dfs(startX+n/2, startY, n/2);
        dfs(startX, startY+n/2, n/2);
        dfs(startX+n/2, startY+n/2, n/2);
    }
}