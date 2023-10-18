// https://school.programmers.co.kr/learn/courses/30/lessons/131127
package CodingTest.Java;

import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class Solution22 {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        
        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        for (int i = 0; i < 10; i++) {
            queue.add(discount[i]);
        }

        for (int i = 10; i <= discount.length; i++) {
            Iterator<String> iter = queue.iterator();
            Map<String, Integer> chkMap = new HashMap<>();
            for (; iter.hasNext();) {
                String s = iter.next();
                if (chkMap.containsKey(s)) {
                    chkMap.put(s, chkMap.get(s) + 1);
                } else {
                    chkMap.put(s, 1);
                }
            }
            if (map.equals(chkMap)) {
                answer += 1;
            }
            if (i < discount.length){
            queue.remove();
            queue.add(discount[i]);
            }
        }
        
        return answer;
    }
}
