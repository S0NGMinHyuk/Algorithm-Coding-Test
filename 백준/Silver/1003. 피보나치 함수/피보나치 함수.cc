#include <iostream>
#include <vector>

using namespace std;

vector<pair<int, int>> getResult(int largest);

int main() {
    int loop;
    cin >> loop;
    
    int largest = 0;
    vector<int> nums;

    for (int i = 0; i < loop; i++) {
        int n;
        cin >> n;
        nums.push_back(n);
        largest = max(largest, n);
    }

    vector<pair<int, int>> result = getResult(largest);
    for (int i : nums) 
        cout << result[i].first << ' ' << result[i].second << '\n';
}

vector<pair<int, int>> getResult(int largest) {
    vector<pair<int, int>> result = {
        {1, 0},
        {0, 1}
    };

    for (int i = 2; i <= largest; i++) {
        pair<int, int> newPair;
        newPair.first = result[i-1].first + result[i-2].first;
        newPair.second = result[i-1].second + result[i-2].second;
        result.push_back(newPair);
    }

    return result;
}