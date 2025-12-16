// 접두어트리 Trie 알고리즘 사용

import java.util.*;

class Solution {
    static class Node {
        Node[] next = new Node[26];
        int cnt = 0;    // 이 노드를 지나간 단어 수
    }
    Node root = new Node();
    
    public int solution(String[] words) {
        int answer = 0;
        
        // 검색어 후보에 추가
        for (String w : words)
            addWord(w);
        
        // 최소 문자수 계산
        for (String w : words)
            answer += findWord(w);
        
        return answer;
    }
    
    public int findWord(String word) {
        Node curr = root;
        for (int i=0; i<word.length(); i++) {
            int idx = word.charAt(i)-'a';
            curr = curr.next[idx];
            if (curr.cnt == 1)
                return i+1;
        }
        return word.length();
    }
    
    public void addWord(String word) {
        Node curr = root;
        for (int i=0; i<word.length(); i++) {
            int idx = word.charAt(i)-'a';
            if (curr.next[idx] == null)
                curr.next[idx] = new Node();
            
            curr = curr.next[idx];
            curr.cnt += 1;
        }
    }
}