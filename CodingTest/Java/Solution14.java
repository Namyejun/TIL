// https://school.programmers.co.kr/learn/courses/30/lessons/12980
package CodingTest.Java;

public class Solution14 {
    public int solution(int n) {
        int ans = 0;
        while (n != 0) {
            if (n % 2 == 1) {
                n -= 1;
                ans += 1;
            } else {
                n /= 2;
            }
        }
        return ans;
    }
}
