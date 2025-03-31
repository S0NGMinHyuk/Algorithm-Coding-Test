#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() 
{
    set<string> notHear;
    vector<string> result;
    int n, m;
    cin >> n >> m;

    string temp;
    for (int i = 0; i<n; i++) { // 못들어본 사람 저장
        cin >> temp;
        notHear.insert(temp);
    }

    for (int i = 0; i<m; i++) { // 못들어본 사람 중 못본 사람 저장
        cin >> temp;
        if (notHear.find(temp) != notHear.end())
            result.push_back(temp);
    }

    sort(result.begin(), result.end()); // 오름차순 정렬
    
    cout << result.size() << '\n';  // 결과 출력
    for (string s : result)
        cout << s << '\n';
}