#include <iostream>
#include <vector>

using namespace std;

// length 길이로 자를 때 얻을 수 있는 나무 길이를 리턴
long long int getTree(vector<long long int> trees, long long int length)
{
    long long int result = 0;
    for (long long int tree : trees) {
        if(tree >= length)
            result += tree - length;
    }
    return result;
}

int main() {
    long long int n, goal;
    vector<long long int> trees;
    cin >> n >> goal;

    long long int small = 0, big = 0;
    for(long long int i=0; i<n; i++) {
        long long int tree;
        cin >> tree;
        trees.push_back(tree);
        big = max(big, tree);
    }

    // 이진탐색 실행
    long long int possible = big;
    while(small <= big) {
        long long int mid = (small+big)/2;

        if(getTree(trees, mid) < goal) big = mid-1; // 목표보다 부족한 경우
        else {
            small = mid+1; // 목표보다 많은 경우
            possible = mid;
        }
    }

    cout << possible;
}