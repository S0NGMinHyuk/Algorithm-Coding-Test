#include <iostream>
#include <queue>
#include <vector>

#define MAX 1001

using namespace std;

int graph[MAX][MAX] = {0,};

int main() {
    int n, e;
    cin >> n >> e;
    
    for(int i=0; i<e; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    vector<int> isUnion(n+1);
    int unions = 0;
    for(int i=1; i<=n; i++) {
        if (isUnion[i] == 0) {
            unions++;
            queue<int> q;
            isUnion[i] = 1;
            q.push(i);

            while(!q.empty()) {
                int now = q.front();
                q.pop();
                for(int node=0; node<=n; node++) {
                    if (graph[now][node] == 1 && isUnion[node] == 0) {
                        isUnion[node] = 1;
                        q.push(node);
                    }
                }
            }
        }
    }
    cout << unions;
}