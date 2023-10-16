// https://school.programmers.co.kr/learn/courses/30/lessons/138476
package CodingTest.Java;

import java.util.Arrays;

public class Solution19 {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int[] map = new int[10000001];
        Arrays.setAll(map, i -> 0);
        for (int i = 0; i < tangerine.length; i++) {
            map[tangerine[i]] += 1;
        }
        Arrays.sort(map);
        for (int i = map.length - 1; i >= 0; i--){
            k -= map[i];
            if (map[i] != 0) answer += 1;
            if (k <= 0) {
                break;
            }
        }
        return answer;
    }
}
