#include <iostream>
#include <string>
#include <stack>


using namespace std;

int main() {
    int loop, input, result, isPrint = 0; 
    stack<int> stack;   // 스택 변수
    string cmd;         // 명령어 변수

    cin >> loop;        // 반복횟수 입력받기
    for (int i = 0; i < loop; i++) {
        cin >> cmd;     // 명령어 입력받기
        isPrint = 1;

        // 명령어에 맞는 기능 수행
        if (cmd == "push") {
            isPrint = 0;    // push 명령어는 출력 X
            cin >> input;
            stack.push(input);
        }
        else if (cmd == "pop") {
            if (stack.empty()) result = -1; // 빈 스택인 경우 -1 출력
            else {
                result = stack.top();       // c++의 pop 함수는 리턴이 없다.
                stack.pop();
            }
        }
        else if (cmd == "size") {
            result = stack.size();
        }
        else if (cmd == "empty") {
            result = stack.empty();
        }
        else if (cmd == "top") {
            if (stack.empty()) result = -1; // 빈 스택인 경우 -1 출력
            else result = stack.top();
        }

        if (isPrint) cout << result << "\n"; // 결과 출력

    }
}