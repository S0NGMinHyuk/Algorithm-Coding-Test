#include <iostream>

using namespace std;

int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) 
        result = result * i;
    return result;
}

int main() {
    int a, b, result = 1;
    cin >> a >> b;
    cout << factorial(a) / (factorial(b) * factorial(a-b));
}