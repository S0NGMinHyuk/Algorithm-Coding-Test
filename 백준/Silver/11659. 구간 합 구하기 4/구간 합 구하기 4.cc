#include <iostream>
#include <vector>

using namespace std;

int main()
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    int nums, testCase;
    cin >> nums >> testCase;

    vector<int> v = {0};
    for(int i=0; i<nums; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp + v[i]);
    }

    for(int i=0; i<testCase; i++) {
        int a, b;
        cin >> a >> b;
        cout << v[b] - v[a-1] << '\n';
    }
}