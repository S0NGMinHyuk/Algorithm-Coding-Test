#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    vector<pair<int,int>> p;    // 2차원 배열 생성
    int loop;
    cin >> loop;

    // 2차원 배열에 값 저장. make_pair() 사용
    for (int i = 0; i < loop; i++) {
        int a, b;
        cin >> a >> b;
        p.push_back(make_pair(a, b));
    }

    // 첫번째 값으로 오름차순 정렬 후 두번째 값으로 오름차순 정렬
    sort(p.begin(), p.end());

    for (int i = 0; i < p.size(); i++) {
        cout << p[i].first << ' ' << p[i].second << '\n';
    }
}    