import java.util.*;

class Solution {
    
    static class Node {
        int count = 0;
        Map<Character, Node> child = new HashMap<>();
    }
    
    Map<Integer, Node> forwardTrie = new HashMap<>();
    Map<Integer, Node> backwardTrie = new HashMap<>();
    
    public int[] solution(String[] words, String[] queries) {
        // 트리 생성
        for (String word : words) {
            
            // 정방향, 역방향 트리의 루트노드 찾기
            forwardTrie.putIfAbsent(word.length(), new Node());
            backwardTrie.putIfAbsent(word.length(), new Node());
            
            Node forwardParent = forwardTrie.get(word.length());
            Node backwardParent = backwardTrie.get(word.length());
            
            forwardParent.count++;
            backwardParent.count++;
            
            for (int i=0; i<word.length(); i++) {
                // 정방형 트라이 채우기
                Character c = word.charAt(i);
                forwardParent.child.putIfAbsent(c, new Node());
                Node next = forwardParent.child.get(c);
                next.count++;
                forwardParent = next;
                
                // 역방향 트라이 채우기
                c = word.charAt(word.length()-i-1);
                backwardParent.child.putIfAbsent(c, new Node());
                next = backwardParent.child.get(c);
                next.count++;
                backwardParent = next;
            }
        }
        
        List<Integer> result = new ArrayList<>();
        for (String query : queries) {
            // 뒷자리가 ?인 쿼리 처리
            Node curr = null;
            
            // 전부 ?인 쿼리
            if (query.charAt(query.length()-1) == '?' && query.charAt(0) == '?') {
                curr = forwardTrie.get(query.length());
                if (curr == null) {
                    result.add(0);
                    continue;
                }
                result.add(curr.count);
                continue;
            // 뒷자리가 ?인 쿼리
            } else if (query.charAt(query.length()-1) == '?') {
                curr = forwardTrie.get(query.length());
                if (curr == null) {
                    result.add(0);
                    continue;
                }
                for (int j=0; j<query.length(); j++) {
                    Character nextChar = query.charAt(j);
                    if (nextChar == '?') {
                        result.add(curr.count);
                        break;
                    } else {
                        Node next = curr.child.get(nextChar);
                        if (next != null)
                            curr = next;
                        else {
                            result.add(0);
                            break;
                        }             
                    }
                }
            // 앞자리가 ?인 쿼리
            } else if (query.charAt(0) == '?') {
                curr = backwardTrie.get(query.length());
                if (curr == null) {
                    result.add(0);
                    continue;
                }
                for (int j=1; j<=query.length(); j++) {
                    Character nextChar = query.charAt(query.length()-j);
                    if (nextChar == '?') {
                        result.add(curr.count);
                        break;
                    } else {
                        Node next = curr.child.get(nextChar);
                        if (next != null)
                            curr = next;
                        else {
                            result.add(0);
                            break;
                        }
                    }
                }
            // ?가 없는 쿼리
            } else {
                curr = forwardTrie.get(query.length());
                if (curr == null) {
                    result.add(0);
                    continue;
                }
                for (int j=0; j<query.length()-1; j++) {
                    Character nextChar = query.charAt(j);
                    Node next = curr.child.get(nextChar);
                    if (next != null)
                        curr = next; 
                    else {
                        result.add(0);
                        break;
                    }
                }
                result.add(curr.count);
            }
        }
        
        int[] array = new int[result.size()];
        for (int i=0; i<result.size(); i++) {
            array[i] = result.get(i);
        }
        return array;
    }
}