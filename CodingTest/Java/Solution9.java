// https://school.programmers.co.kr/learn/courses/30/lessons/181188
package CodingTest.Java;

import java.util.Arrays;
import java.util.Comparator;
class Solution9 {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, Comparator.comparingInt((int[] i) -> i[1]));
        double shoot = -1;
        for (int[] target : targets) {
            if (target[0] > shoot) {
                answer += 1;
                shoot = target[1] - 0.5;
            }
        }

        return answer;
    }
}
// 나 진짜 멍청하네