#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int loop;
    cin >> loop;

    // 회원 정보 입력
    vector<pair<pair<int, string>, int>> data;
    for (int i = 0; i < loop; i++) {
        int age;
        string name;
        cin >> age >> name;
        data.push_back(make_pair(make_pair(age, name), i));
    }

    // 람다식을 사용한 정렬
    sort(data.begin(), data.end(), [](const auto &x, const auto &y) {
        if (x.first.first == y.first.first) {
            return x.second < y.second;
        }
        return x.first.first < y.first.first;
    });
    
    // 답 출력
    for (int i = 0; i < data.size(); i++)
        cout << data[i].first.first << ' ' << data[i].first.second << '\n';
}