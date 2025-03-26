#include <iostream>
#include <vector>

using namespace std;

// 티셔츠를 T장씩 주문해야 하는 묶음 출력
void print_T(vector<int> v, int t) {
    int result = 0;
    for (int i = 0; i < 6; i++) {
        if (v[i] % t == 0) result += v[i] / t;
        else result += v[i] / t + 1;
    }
    cout << result << "\n";
    return;
}

// 펜을 P개씩 주문해야 하는 묶음과 단품 개수 출력
void print_P(int n, int p) {
    cout << n / p << " " << n % p;
}

int main() {
    int n;
    cin >> n;

    // 사이즈별 개수 저장
    vector<int> v;
    for (int i = 0; i < 6; i++) {
        int shirt;
        cin >> shirt;
        v.push_back(shirt);
    }
    
    int t, p;
    cin >> t >> p;

    print_T(v, t);
    print_P(n, p);
}