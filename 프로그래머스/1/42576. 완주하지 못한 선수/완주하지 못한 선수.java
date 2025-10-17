// String은 .equals() 로 비교
// HashMap에서 .getOrDefault(key, 0) 기능 있음
// HashMap에서 value 갱신할때도 put으로 넣어야함.

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }
        return participant[participant.length-1];
    }
}

class Solution2 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();

        // 참가자 명단 추가
        for (String name : participant) {
            map.put(name, map.getOrDefault(name, 0) + 1);
        }

        // 완주한 사람 차감
        for (String name : completion) {
            map.put(name, map.get(name) - 1);
        }

        // 값이 1인 사람 = 완주 못한 사람
        for (String name : participant) {
            if (map.get(name) > 0) {
                return name;
            }
        }
        return null;
    }
}