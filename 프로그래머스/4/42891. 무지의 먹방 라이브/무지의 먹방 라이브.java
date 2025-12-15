import java.util.*;

class Info implements Comparable<Info> {
    int index;
    int time;
    
    public Info(int i, int t) {
        index = i;
        time = t;
    }
    
    public int compareTo(Info target) {
        if (this.time == target.time)
            return this.index < target.index ? -1 : 1;
        return this.time < target.time ?-1 : 1;
    }
    
    public int getTime()  {return this.time;}
    public int getIndex() {return this.index;}
}


class Solution {
    public int solution(int[] food_times, long k) {
        Queue<Info> heap = new PriorityQueue<>();
        for (int ft : food_times) {
            heap.add(new Info(heap.size()+1, ft));
        }
        
        int lastFoodTime = 0;
        while (!heap.isEmpty()) {
            long diff = (long) heap.peek().getTime() - lastFoodTime; // long
            long spend = diff * heap.size();                         // long
            if (spend > k) 
                break;
            k -= spend;
            lastFoodTime = heap.poll().getTime();
        }
        
        if (heap.isEmpty())
            return -1;
        
        int[] arr = new int[heap.size()];
        for (int i=0; i<arr.length; i++) 
            arr[i] = heap.poll().getIndex();
        
        Arrays.sort(arr);
        int idx = (int)(k % arr.length);
        return arr[idx];
    }
}