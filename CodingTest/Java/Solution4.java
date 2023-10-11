// https://school.programmers.co.kr/learn/courses/30/lessons/70129
package CodingTest.Java;

public class Solution4 {
    public int[] solution(String s) {
        int[] answer = {};
        int remove0 = 0;
        int times = 0;
        while (true) {
            if (s.equals("1")) {
                break;
            }
            times += 1;
            int ogLen = s.length();
            s = s.replace("0","");
            int tempS = s.length();
            remove0 += ogLen - tempS;
            String binaryString = Integer.toBinaryString(tempS);
            s = binaryString;
        }
        answer = new int[] {times, remove0};
        return answer;
    }
}
