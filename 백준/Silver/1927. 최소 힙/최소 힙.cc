#include <iostream>
#include <queue>

using namespace std;

int main() 
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    // 오름차순 힙 생성 (기본값은 내림차순)
    priority_queue<int, vector<int>, greater<int>> heap; 
    int loop, num;
    cin >> loop;

    for(int i=0; i<loop; i++) {
        cin >> num;
        
        if(num != 0) heap.push(num);
        else {
            if(heap.size() == 0) cout << 0 << '\n';
            else {
                cout << heap.top() << '\n';
                heap.pop();
            }
        }
    }
}