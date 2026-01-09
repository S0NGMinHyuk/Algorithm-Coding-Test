// 숫자를 사전순 문자열로 바꿀때는 26으로 나눈 나머지가 0인 경우를 생각해야한다.

import java.util.*;

class Solution {
    public String solution(long n, String[] bans) {
        // 금지 스펠을 숫자로 바꾸기
        List<Long> removed = new ArrayList<>();
        for (String b : bans) {
            removed.add(spellToNumber(b));
        }
        
        // 금지 스펠 정렬
        Collections.sort(removed);
        
        // n이 금지 스펠 숫자보다 크거나 같으면 n++
        for (Long banSpellNumber : removed) {
            if (n >= banSpellNumber)
                n++;
            else
                break;
        }

        return numberToSpell(n);
    }
    
    // 주문을 숫자로 변경
    public long spellToNumber(String spell) {
        long number = 0;
        for (int i=0; i<spell.length(); i++) {
            char c = spell.charAt(spell.length()-i-1);
            number += (c-'a'+1) * Math.pow(26, i);
        }
        return number;
    }
    
    // 숫자를 주문으로 변경
    public String numberToSpell(long number) {
        StringBuilder sb = new StringBuilder();
        while (number > 0) {
            int rest = (int) (number % 26);
            if (rest == 0) {    // 나머지가 0인 경우, z 가 들어가야 한다.
                sb.append('z');
                number--;
            } else {
                sb.append((char) (rest+'a'-1));    
            }
            number = number / 26L;
        }
        return sb.reverse().toString();
    }
}