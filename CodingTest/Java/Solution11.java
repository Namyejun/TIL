// https://school.programmers.co.kr/learn/courses/30/lessons/12945
package CodingTest.Java;

class Solution11 {
    public int solution(int n) {
        int[] fibb = new int[100001];
        fibb[0] = 0;
        fibb[1] = 1;
        for (int i = 2; i < 100001; i++) {
            fibb[i] = (fibb[i - 2] + fibb[i - 1]);
        }

        return fibb[n] % 1234567;
    }
}