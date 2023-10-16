// https://school.programmers.co.kr/learn/courses/30/lessons/131701
package CodingTest.Java;

import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class Solution20 {
    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i: elements) queue.add(i);

        for (int i = elements.length; i >= 1; i--) {
            for (int j = 0; j < elements.length; j++) {
                int temp = 0;
                Iterator<Integer> iter = queue.iterator();
                for (int t = i; t > 0; t--) {
                    temp += iter.next();
                }
                set.add(temp);
                queue.add(queue.remove());
            }
        }
        answer = set.size();
        return answer;
    }
}
