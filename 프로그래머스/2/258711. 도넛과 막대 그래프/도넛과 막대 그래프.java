import java.util.*;

// 도넛 모양 그래프는 모든 노드가 inDegree == outDegree == 1
// 막대 모양 그래프는 끝노드 기준 outDegree = 0
// 8자 모양 그래프는 특정노드 기준 inDegree = 2, outDegree = 2
// 생성 정점 노드는 inDegree = 0, outDegree >= 2

class Solution {
    
    static class Node {
        int inDegree = 0;
        List<Integer> child = new ArrayList<>();
    }
    
    int[] answer = new int[]{0, 0, 0, 0};
    Map<Integer, Node> map = new HashMap<>();
    
    public int[] solution(int[][] edges) {
        
        // 그래프 정보 저장
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            
            map.putIfAbsent(from, new Node());
            map.putIfAbsent(to, new Node());
            
            // 자식 노드 저장 & inDegree 갱신
            map.get(from).child.add(to);
            map.get(to).inDegree++;
        }

        // 생성 정점 노드 찾기
        // 생성 정점 노드는 inDegree = 0, outDegree >= 2
        for (Integer key : map.keySet()) {
            Node node = map.get(key);
            if (node.inDegree == 0 & node.child.size() >= 2) {
                answer[0] = key;
                break;
            }
        }
        
        // 생성 정점에 이어진 그래프들 순회하기
        for (int start : map.get(answer[0]).child) {
            Node curr = map.get(start);
            
            while (true) {
                if (curr.child.size() == 0) {  // 막대모양 그래프의 끝노드인 경우
                    answer[2]++;
                    break;
                } else if (curr.child.size() == 2) {  // 8자모양 그래프의 중앙노드인 경우
                    answer[3]++;
                    break;
                } else {
                    if (curr.child.get(0) == start) {  // 도넛모양 그래프인 경우 (원위치)
                        answer[1]++;
                        break;
                    }
                    curr = map.get(curr.child.get(0));  // 다음 노드로 이동
                }
            }
        }
        return answer;
    }
}
