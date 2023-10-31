// https://school.programmers.co.kr/learn/courses/30/lessons/92335
package CodingTest.Java;

import java.util.Arrays;

public class Solution30 {
    public int solution(int n, int k) {
        int answer = 0;
        StringBuffer sb = new StringBuffer();
        while (n != 0) {
            sb.append(n%k);
            n /= k;
        }
        
        long[] arr = Arrays.stream(sb.reverse().toString().split("[0]+")).mapToLong(Long::parseLong).toArray();
        Arrays.stream(arr).forEach(i -> System.out.println(i));
        for (long i : arr) {
            boolean chk = true;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    chk = false;
                    break;
                }
            }
            if (i >= 2 && chk) answer += 1;
        }
        return answer;
    }
}
// int의 범위에 대해서 생각해 볼 필요가 있음, long 사용하는 방법 있음