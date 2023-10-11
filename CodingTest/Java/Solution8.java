// https://school.programmers.co.kr/learn/courses/30/lessons/176962
package CodingTest.Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Stack;

class Solution8 {
    public static int convertTime(String time) {
        String[] temp = time.split(":");
        return Integer.parseInt(temp[0]) * 60 + Integer.parseInt(temp[1]);
    }
    
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        
        Stack<String[]> readyStack = new Stack<>();

        Arrays.sort(plans, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                return convertTime(o1[1]) - convertTime(o2[1]);
            }
        });

        int leftTime = 0;

        for (int i = 0; i < plans.length; i++) {
            String name = plans[i][0];
            int start = convertTime(plans[i][1]);
            int playtime = Integer.parseInt(plans[i][2]);

            while (readyStack.size() != 0) {
                String[] temp = readyStack.pop();
                String n = temp[0];
                int pt = Integer.parseInt(temp[1]);

                if (leftTime >= pt) {
                    leftTime -= pt;
                    answer.add(n);
                } else {
                    readyStack.push(new String[]{n, String.valueOf(pt - leftTime)});
                    break;
                }
            }

            readyStack.push(new String[]{name, String.valueOf(playtime)});

            if (i < plans.length - 1) {
                int nextStart = convertTime(plans[i+1][1]);
                leftTime = nextStart - start;
            }
        }
        
        while (readyStack.size() != 0) {
            String[] temp = readyStack.pop();
            answer.add(temp[0]);
        }

        return answer.toArray(new String[answer.size()]);
    }
}