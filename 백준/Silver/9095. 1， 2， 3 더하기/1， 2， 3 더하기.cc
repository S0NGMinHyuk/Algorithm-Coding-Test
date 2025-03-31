#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int testCase;
    cin >> testCase;
    for(int i=0; i<testCase; i++) {
        int goal;
        cin >> goal;
        vector<int> dp = {0, 1, 2, 4};
        
        for(int j=4; j<=goal; j++) {
            dp.push_back(dp[j-1] + dp[j-2] + dp[j-3]);
        }

        cout << dp[goal] << '\n';
    }
}