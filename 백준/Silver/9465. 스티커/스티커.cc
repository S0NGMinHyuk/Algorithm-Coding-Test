#include <iostream>
#include <vector>

using namespace std;

void testCase()
{
    int l;
    cin >> l;
    vector<vector<int>> sticker;

    // 스티커 이차원 배열 생성
    for(int i=0; i<2; i++) {
        vector<int> temp(l);
        for(int j=0; j<l; j++) {
            cin >> temp[j];
        }
        sticker.push_back(temp);
    }

    for(int j=0; j<2; j++) {
        int index = (j == 0 ? 1 : 0);
        sticker[j][1] += sticker[index][0];
    }

    for(int i=2; i<l; i++) {
        for(int j=0; j<2; j++) {
            int index = (j == 0 ? 1 : 0);
            // 대각선, 대각선의 왼쪽(체스의 나이트처럼) 비교
            sticker[j][i] += max(sticker[index][i-1], sticker[index][i-2]);
        }
    }

    // 최대값 리턴
    cout << max(sticker[0][l-1], sticker[1][l-1]) << '\n';
}

int main()
{
    int n;
    cin >> n;
    for(int i=0; i<n; i++) {
        testCase();
    }
}