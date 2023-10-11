// https://school.programmers.co.kr/learn/courses/30/lessons/12951
package CodingTest.Java;

public class Solution2 {
    public String solution(String s) {
        String answer = "";
        String[] temp = s.split("");
        boolean check = true;
        for (int i = 0; i < temp.length; i++) {
            if (check) {
                if (temp[i].equals(" ")) {
                    
                } else {
                    temp[i] = temp[i].toUpperCase();
                    check = false;
                }
            } else {
                if (temp[i].equals(" ")) {
                    check = true;
                } else {
                    temp[i] = temp[i].toLowerCase();
                }
            }
            answer += temp[i];
        }
        return answer;
    }
}
