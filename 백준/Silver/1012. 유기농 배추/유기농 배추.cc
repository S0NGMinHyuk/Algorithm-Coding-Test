#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void solution();
void findArea(int i, int j, int width, int height);

int visited[50][50];
int graph[50][50];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int main() 
{
    int loop;
    cin >> loop;
    for(int i=0;i<loop;i++)
        solution();
}

void solution() // 각 테스트케이스에 맞는 답 구하는 함수
{
    // 배열 변수 초기화 함수
    fill(&visited[0][0], &visited[0][0]+50*50, 0);
    fill(&graph[0][0], &graph[0][0]+50*50, 0);

    int w, h, n, r, c, result = 0;
    cin >> w >> h >> n;

    // 배추가 있는 위치를 graph에 추가
    for(int i=0;i<n;i++) {
        cin >> r >> c;
        graph[r][c] = 1;
    }

    // graph 배열을 돌며 배추흰지렁이가 없는 영역의 배추 발견 시 findArea 함수 호출
    for(int i=0; i<w; i++) {
        for(int j=0; j<h; j++) {
            if (graph[i][j] == 1 && visited[i][j] == 0) {
                findArea(i, j, w, h);
                result++;
            }
        }
    }

    cout << result << '\n'; // 결과 출력
}

void findArea(int i, int j, int width, int height) // 배추흰지렁이를 둬야 하는 영역을 구하는 함수
{
    queue<pair<int, int>> q;
    q.push(make_pair(i, j));

    // BFS 알고리즘 사용
    int r, c;
    while (q.size() > 0) {
        r = q.front().first;
        c = q.front().second;
        q.pop();
        visited[r][c] = 1;

        for(int i=0; i<4; i++) {
            if ((r+dx[i] >= 0 && r+dx[i] < width && c+dy[i] >= 0 && c+dy[i] < height)
            && graph[r+dx[i]][c+dy[i]] ==1 
            && visited[r+dx[i]][c+dy[i]] == 0) {
                q.push(make_pair(r+dx[i], c+dy[i]));
                visited[r+dx[i]][c+dy[i]] = 1;
            }
        }
    }
}