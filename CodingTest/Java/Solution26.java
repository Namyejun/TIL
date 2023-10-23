// https://school.programmers.co.kr/learn/courses/30/lessons/64065
package CodingTest.Java;

import java.util.Arrays;
import java.util.Comparator;

public class Solution26 {
    public int[] solution(String s) {
        String t = s.substring(2, s.length() - 2);
        String[] temp = t.split("\\},\\{");
        int[] answer = new int[temp.length];
        Arrays.sort(temp, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.length() - o2.length();
            }
        });
        
        answer[0] = Integer.parseInt(temp[0]);

        for (int i = 1; i < temp.length; i++) {
            int sumOfTemp = Arrays.stream(temp[i].split(",")).mapToInt(Integer::parseInt).sum();
            for (int j = 0; j < i; j++) {
                sumOfTemp -= answer[j];
            }
            answer[i] = sumOfTemp;
        }

        return answer;
    }
}