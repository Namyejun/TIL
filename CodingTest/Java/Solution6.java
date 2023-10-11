// https://school.programmers.co.kr/learn/courses/30/lessons/178870
package CodingTest.Java;

class Solution6 {
    public static int[] solution(int[] sequence, int k) {
        int[] answer = new int[] {};
        int start = 0;
        int end = 0;
        int temp = sequence[0];
        int tempLen = 99999999;
        while (true) {
            if (temp < k) {
                end += 1;
                if (start >= sequence.length || end >= sequence.length) {
                    break;
                }
                temp += sequence[end];
            } else if (temp == k) {
                if (tempLen > end - start) {
                    tempLen = end - start;
                    answer = new int[] {start, end};
                }
                if (end < sequence.length - 1) {
                    end += 1;
                    temp += sequence[end];
                } else {
                    temp -= sequence[start];
                    start += 1;
                }
            } else {
                temp -= sequence[start];
                start += 1;
                if (start >= sequence.length || end >= sequence.length) {
                    break;
                }
            }
        }
        
        return answer;
    }
}
