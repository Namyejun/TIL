// https://school.programmers.co.kr/learn/courses/30/lessons/12953
package CodingTest.Java;

public class Solution17 {
    public int solution(int[] arr) {
        int lcm = arr[0];
        for (int i = 1; i < arr.length; i++) {
            int temp = lcm;
            while(lcm % arr[i] != 0) {
                lcm += temp;
            }
        }
        return lcm;
    }
}
