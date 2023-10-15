// https://school.programmers.co.kr/learn/courses/30/lessons/12985
package CodingTest.Java;

public class Solution16 {
    public int solution(int n, int a, int b) {
        int answer = 1;
        a -= 1;
        b -= 1;

        while (a != b) {
            a = a / 2;
            b = b / 2;
            
            answer += 1;
        }
        return answer - 1;
    }
}