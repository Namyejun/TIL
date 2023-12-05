// https://school.programmers.co.kr/learn/courses/30/lessons/150370
package CodingTest.Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution31 {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] todays = Arrays.stream(today.split("\\.")).mapToInt(Integer::parseInt).toArray();
        long todaysDays = todays[0]*12*28 + todays[1]*28 + todays[2];
        Map<String, Integer> termsMap = new HashMap<>();
        for (String input : terms) {
            String[] inputs = input.split(" ");
            termsMap.put(inputs[0], Integer.parseInt(inputs[1]));
        }
        int t = 1;
        for (String input : privacies) {
            String[] inputs = input.split(" ");

            int[] contDay = Arrays.stream(inputs[0].split("\\.")).mapToInt(Integer::parseInt).toArray(); // 계약일
            String term = inputs[1]; // 약관 종류

            long contDays = contDay[0]*12*28 + contDay[1]*28 + contDay[2] + termsMap.get(term)*28 - 1;

            if (todaysDays > contDays) {
                answer.add(t);
            }
            t++;
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}