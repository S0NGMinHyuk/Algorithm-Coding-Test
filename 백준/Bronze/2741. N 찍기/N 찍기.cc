#include <iostream>
using  namespace  std;

int main() {
	// 입출력 속도 줄이기 + endl -> \n
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int user = 0;
	cin >> user;

	for (int i = 1; i <= user; i++) { cout << i << "\n"; }
}