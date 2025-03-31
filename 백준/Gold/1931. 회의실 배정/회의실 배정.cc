#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() 
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    int loop, count = 0;
    vector<pair<int, int>> classes;
    cin >> loop;

    for(int i=0;i<loop;i++) {
        int a, b;
        cin >> a >> b;
        classes.push_back(make_pair(b, a)); // {종료시간, 시작시간} 형태로 저장
    }

    sort(classes.begin(), classes.end());   // 종료시간이 빠른 순서 & 시작시간이 빠른 순서대로 저장

    int index = 0, possible = 0;
    while(index < loop){
        if (classes[index].second >= possible) {    // 현재 수업을 할 수 있는 경우
            possible = classes[index].first;        // 해당 수업의 종료시간을 저장
            count++;
        }
        index++;
    }

    cout << count;
}