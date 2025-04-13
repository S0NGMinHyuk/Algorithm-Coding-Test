#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int l;
    cin >> l;

    vector<int> list(l);
    vector<int> dp(l, 1);
    for(int i=0; i<l; i++) cin >> list[i];

    int result = 0;
    for(int i=0; i<l; i++) {
        for(int j=0; j<i; j++) {
            if (list[j] < list[i] && dp[j]+1 > dp[i]) {
                dp[i] = dp[j]+1;
            }
        }
        result = max(result, dp[i]);
    }

    cout << result;
    return 0;
}