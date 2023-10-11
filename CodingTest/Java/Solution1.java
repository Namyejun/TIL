// https://school.programmers.co.kr/learn/courses/30/lessons/12939
package CodingTest.Java;

import java.util.Arrays;
import java.util.Iterator;

class Solution1 {
    public String solution(String s) {
        String answer = "";
        String[] splitS = s.split(" ");
        int minNum = 99999;
        int maxNum = -99999;

        Iterator<Integer> iter = Arrays.stream(splitS).map((i) -> {
            return Integer.parseInt(i);
        }).iterator();

        while (iter.hasNext()){
            int i = iter.next();
            if (i < minNum) {
                minNum = i;
            }
            if (i > maxNum) {
                maxNum = i;
            }

        }

        answer = String.valueOf(minNum) + " " + String.valueOf(maxNum);
        return answer;
    }
}
