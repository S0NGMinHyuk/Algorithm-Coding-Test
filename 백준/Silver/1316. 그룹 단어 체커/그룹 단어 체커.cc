#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    int loop, result;
    string word;
    cin >> loop;
    result = loop;

    for (int i = 0; i < loop; i++) {
        set<char> alphabet;
        cin >> word;
        for (int j = 0; j < word.size(); j++) {
            if (j == 0) {
                alphabet.insert(word[j]);
                continue;
            }
            if (word[j] != word[j-1]) {
                if (alphabet.find(word[j]) != alphabet.end()) {
                    result--;
                    break;
                }
                else {
                    alphabet.insert(word[j]);
                }
            }
        }
    }
    
    cout << result;
    return 0;
}