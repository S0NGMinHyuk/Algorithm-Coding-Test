#include <iostream>
#include <vector>

using namespace std;

int main() {
    int goal;
    cin >> goal;

    vector<int> vector(goal + 1);   // 벡터 선언

    for (int i = 1; i < vector.size(); i++) {
        if (i == 1) vector[i] = 0;
        else if (i == 2 || i == 3) vector[i] = 1;
        else {
            if (i % 6 == 0) {
                vector[i] = min(min(vector[i-1], vector[i/2]), vector[i/3]) + 1;
            }
            else if (i % 2 == 0) {
                vector[i] = min(vector[i-1], vector[i/2]) + 1;
            }
            else if (i % 3 == 0) {
                vector[i] = min(vector[i-1], vector[i/3]) + 1;
            }
            else {
                vector[i] = vector[i-1] + 1;
            }
        }
    }
    
    cout << vector[goal];

}