// https://school.programmers.co.kr/learn/courses/30/lessons/42885
package CodingTest.Java;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

public class Solution15 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        Deque<Integer> queue = new LinkedList<>();
        for(int i = 0; i < people.length; i++) {
            queue.addLast(people[i]);
        }

        while (!queue.isEmpty()) {
            if (queue.size() == 1) {
                queue.removeLast();
                answer += 1;
            } else {
                if (queue.getFirst() + queue.getLast() > limit) {
                    queue.removeLast();
                    answer += 1;
                } else {
                    queue.removeFirst();
                    queue.removeLast();
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}