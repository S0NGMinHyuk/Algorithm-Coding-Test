#include <iostream>
#include <vector>

#define R 0
#define G 1
#define B 2

using namespace std;

vector<vector<int>> houses;
int result[3] = {0, 0, 0};

int main() 
{
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
    ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    int n;
    cin >> n;

    for(int i=0; i<n; i++) {
        vector<int> temp(3);
        for(int j=0; j<3; j++) {
            cin >> temp[j];
        }
        houses.push_back(temp);
    }

    result[R] = houses[0][R];
    result[G] = houses[0][G];
    result[B] = houses[0][B];

    for(int i=1; i<houses.size(); i++) {
        int r, g, b;
        r = houses[i][R] + min(result[G], result[B]);
        g = houses[i][G] + min(result[R], result[B]);
        b = houses[i][B] + min(result[R], result[G]);

        result[R] = r;
        result[G] = g;
        result[B] = b;
    }

    cout << min(min(result[R], result[G]), result[B]);
}