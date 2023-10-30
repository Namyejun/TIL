// https://school.programmers.co.kr/learn/courses/30/lessons/43105
package CodingTest.Java;

public class Solution29 {
    public int solution(int[][] triangle) {
        int answer = 0;
        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        return triangle[0][0];
    }
}
