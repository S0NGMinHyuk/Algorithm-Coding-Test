#include <iostream>
#include <vector>

using namespace std;

void printVector(vector<int> v) 
{
    for(int i=0; i<v.size(); i++) {
        cout << v[i] << ' ';
    }
    cout << '\n';
    return;
}

void dfs(int index, int n, int m, vector<int> v)
{
    if(index > n) {
        if(v.size() == m)
            printVector(v);
        return;
    }

    if(v.size() < m) {
        v.push_back(index);
        dfs(index+1, n, m, v);
        v.pop_back();
    }
    dfs(index+1, n, m, v);
}

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> v;
    dfs(1, n, m, v);
}