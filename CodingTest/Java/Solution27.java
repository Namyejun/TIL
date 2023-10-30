// https://school.programmers.co.kr/learn/courses/30/lessons/17677
package CodingTest.Java;

import java.util.ArrayList;
import java.util.List;

public class Solution27 {
    public int solution(String str1, String str2) {
        List<String> inter = new ArrayList<>();
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        int str1Len = 0;
        int str2Len = 0;
        for (int i = 0; i < str1.length() - 1; i++) {
            String s = str1.substring(i, i + 2);
            if ('A' <= s.charAt(0) && s.charAt(0) <= 'Z' && 'A' <= s.charAt(1) && s.charAt(1) <= 'Z' ) {
                inter.add(s);
                str1Len += 1;
            }
        }

        int interVal = 0;


        for (int i = 0; i < str2.length() - 1; i++) {
            String s = str2.substring(i, i + 2);
            if ('A' <= s.charAt(0) && s.charAt(0) <= 'Z' && 'A' <= s.charAt(1) && s.charAt(1) <= 'Z' ) {
                str2Len += 1;
                if (inter.contains(s)) {
                    inter.remove(s);
                    interVal += 1;
                }
            }
        }
        if (str1Len == 0 && str2Len == 0) {
            return 65536;
        }
        return  (int) (65536*((float) interVal / (float) (str1Len + str2Len - interVal)));
    }
}
