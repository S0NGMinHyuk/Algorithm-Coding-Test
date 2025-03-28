#include <iostream>
#include <string>
#include <set>


using namespace std;

int main() {
    cin.tie(NULL);                      // 입력과 출력 연결을 끊어준다
	ios_base::sync_with_stdio(false);   // C의 stdio와 C++의 iostream의 동기화를 비활성화

    int loop, input, result;
    bool isPrint; 
    set<int> set;   // 집합 변수
    string cmd;     // 명령어 변수

    cin >> loop;        // 반복횟수 입력받기
    for (int i = 0; i < loop; i++) {
        cin >> cmd;     // 명령어 입력받기
        isPrint = false;

        // 명령어에 맞는 기능 수행
        if (cmd == "add") {
            cin >> input;
            set.insert(input);
        }
        else if (cmd == "remove") {
            cin >> input;
            set.erase(input);
        }
        else if (cmd == "check") {
            isPrint = true;
            cin >> input;
            if (set.find(input) != set.end())
                result = 1;
            else
                result = 0;
        }
        else if (cmd == "toggle") {
            cin >> input;
            if (set.find(input) != set.end())
                set.erase(input);
            else
                set.insert(input);
        }
        else if (cmd == "all") {
            set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
        }
        else if (cmd == "empty") {
            set.clear();
        }

        if (isPrint) cout << result << "\n"; // 결과 출력

    }
}