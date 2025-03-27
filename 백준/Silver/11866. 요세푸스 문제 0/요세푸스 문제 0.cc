#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> answer;
    vector<int> v(n);
    for (int i = 0; i < n; i++) v[i] = i+1; // N명의 사람 추가

    int index = 0, cnt = 1;
    while(v.size()) {
        if (cnt == k) {
            answer.push_back(v[index]);     // 요세푸스 순열대로 저장
            v.erase(v.begin() + index);
            cnt = 1;
        }
        else {
            cnt++;
            index++;
            index %= v.size();
        }
    }

    // 답 출력
    cout << "<";
    for (int i = 0; i < answer.size(); i++) {
        cout << answer[i];
        if (i != answer.size() - 1) {
            cout << ", ";
        }
    }
    cout << ">";
}