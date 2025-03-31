#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> v = {0, 1, 2};
    for (int i=3; i<=n; i++) {
        v.push_back((v[i-1] + v[i-2]) % 10007);
    }

    cout << v[n];
}