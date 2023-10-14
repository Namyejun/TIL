// https://school.programmers.co.kr/learn/courses/30/lessons/12981
package CodingTest.Java;

import java.util.HashSet;
import java.util.Set;

public class Solution13 {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        char beforeWord = ' ';
        Set<String> set = new HashSet<>();
        for (int i = 0; i < words.length; i++) {
            if (set.contains(words[i]) || (beforeWord != ' ' && beforeWord != words[i].charAt(0))) {
                System.out.println(words[i]);
                answer[0] = i % n + 1;
                answer[1] = (i / n) + 1;
                break;
            } else {
                set.add(words[i]);
                beforeWord = words[i].charAt(words[i].length() - 1);
            }
        } 
        return answer;
    }
}

