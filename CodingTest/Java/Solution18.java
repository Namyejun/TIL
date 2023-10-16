// https://school.programmers.co.kr/learn/courses/30/lessons/12914
package CodingTest.Java;

public class Solution18 {
    public long solution(int n) {
        int[] dp = new int[2001];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < 2001; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
        }
        return dp[n];
    }
}