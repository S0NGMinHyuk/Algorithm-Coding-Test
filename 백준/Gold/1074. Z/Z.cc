#include <iostream>
#include <cmath>

using namespace std;

int n, r, c, result = 0;

void dfs();

int main() 
{
    cin >> n >> r >> c;
    dfs();
    cout << result;    
}

void dfs() 
{
    // 재귀함수 종료조건
    if (r == 0 && c == 0)
        return;
    
    if (r < pow(2, n-1)) {
        if (c >= pow(2, n-1)) { // 4등분했을 때 1사분면인 경우
            result += pow(2, n-1) * pow(2, n-1);
            c -= pow(2, n-1);
        }
        else {} // 4등분했을 때 2사분면인 경우
    }
    else {
        if (c >= pow(2, n-1)) { // 4등분했을 때 4사분면인 경우
            result += 3 * pow(2, n-1) * pow(2, n-1);
            c -= pow(2, n-1);
        }
        else {  // 3등분했을 때 2사분면인 경우
            result += 2 * pow(2, n-1) * pow(2, n-1);
        }
        r -= pow(2, n-1);
    }
    n--;
    dfs();
}