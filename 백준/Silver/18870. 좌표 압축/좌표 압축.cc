#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    int n;
    cin >> n;

    vector<int> numList(n);
    vector<int> tempList;
    set<int> numSet;
    for(int i=0; i<n; i++) {
        int num;
        cin >> num;
        numList[i] = num;
        if(numSet.find(num) == numSet.end()) {
            numSet.insert(num);
            tempList.push_back(num);
        }
    }

    sort(tempList.begin(), tempList.end());

    map<int, int> order;
    for(int i=0; i<tempList.size(); i++)
        order.insert({tempList[i], i});
    
    for(int i=0; i<n; i++)
        cout << order.find(numList[i])->second << ' ';
}