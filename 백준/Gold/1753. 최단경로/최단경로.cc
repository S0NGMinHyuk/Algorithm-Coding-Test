#include <iostream>
#include <vector>
#include <queue>
#include <utility>

#define MAX 10000000

using namespace std;

int main() 
{
    int v, e, k;
    cin >> v >> e >> k;

    vector<vector<pair<int, int>>> graph(v + 1); // 인접 리스트

    for (int i = 0; i < e; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back({b, w});
    }

    vector<int> dist(v + 1, MAX);
    dist[k] = 0;

    // 우선순위 큐: {거리, 노드}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, k});

    while (!pq.empty()) {
        int cost = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (dist[now] < cost) continue;

        for (auto next : graph[now]) {
            int nextNode = next.first;
            int nextCost = cost + next.second;

            if (dist[nextNode] > nextCost) {
                dist[nextNode] = nextCost;
                pq.push({nextCost, nextNode});
            }
        }
    }

    for (int i = 1; i <= v; i++) {
        if (dist[i] == MAX) cout << "INF\n";
        else cout << dist[i] << '\n';
    }

    return 0;
}
