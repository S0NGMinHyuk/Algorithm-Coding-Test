#include <iostream>

using namespace std;

long long dfs(long long a, long long b, long long c) 
{
    if(b==1) return a%c;

    long long k = dfs(a, b/2, c);
    
    if(b%2 == 0) return k * k % c;
    else return k * k % c * a % c;
}

int main() 
{
    long long a, b, c;
    cin >> a >> b >> c;
    cout << dfs(a, b, c);
}