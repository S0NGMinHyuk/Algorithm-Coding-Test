#include <iostream>
#include <queue>

#define MAX 100001

using namespace std;

int arr[MAX];

int main() 
{
    queue<int> q;
    int start, goal;

    fill(arr, arr+MAX, MAX);
    cin >> start >> goal;
    arr[start] = 0;
    q.push(start);

    while(!q.empty()) {
        int now = q.front();
        q.pop();

        // 뒤로 걷기
        if (now-1 >= 0 && arr[now]+1 < arr[now-1]) {
            arr[now-1] = arr[now]+1;
            q.push(now-1);
        }
        // 앞으로 걷기
        if (now+1 < MAX && arr[now]+1 < arr[now+1]) {
            arr[now+1] = arr[now]+1;
            q.push(now+1);
        }
        // 순간이동하기
        if (now*2 < MAX && arr[now]+1 < arr[now*2]) {
            arr[now*2] = arr[now]+1;
            q.push(now*2);
        }
    }

    cout << arr[goal];
}