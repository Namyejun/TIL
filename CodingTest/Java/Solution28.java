// https://school.programmers.co.kr/learn/courses/30/lessons/43165
package CodingTest.Java;

public class Solution28 {
    public static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, 0, target);
        return answer;
    }

    public void dfs(int[] numbers, int pointer, int result, int target) {
        if (pointer == numbers.length && result == target) {
            answer += 1;
        }
        if (!(pointer >= numbers.length)) {
            for (int i = 0; i < 2; i++) {
                if (i == 0) {
                    dfs(numbers, pointer + 1, result + numbers[pointer], target);
                } else {
                    dfs(numbers, pointer + 1, result - numbers[pointer], target);
                }
            }   
        }
    }
}
