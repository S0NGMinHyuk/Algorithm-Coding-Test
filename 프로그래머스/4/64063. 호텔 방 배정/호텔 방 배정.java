import java.util.*;

class Solution {
    Map<Long, Long> rooms = new HashMap<>();
    
    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        int idx = 0;
        
        for (long n : room_number) 
            answer[idx++] = getRoom(n);

        return answer;
    }
    
    // 유니온파인드 알고리즘
    long getRoom(long n) {
        if (!rooms.containsKey(n)) { // 방이 비어있는 경우
            rooms.put(n, n+1);
            return n;
        }
        else {  // 방이 차있는 경우
            long nextRoomNumber = getRoom(rooms.get(n));
            rooms.put(n, nextRoomNumber);
            return nextRoomNumber;
        }
    }
}