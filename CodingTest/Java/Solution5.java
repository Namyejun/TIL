// https://school.programmers.co.kr/learn/courses/30/lessons/12924
package CodingTest.Java;

class Solution5 {
    public int solution(int n) {
        int answer = 0;
        int[] arr = new int[n + 1];
        // Arrays.setAll(arr, i -> IntStream.range(0, i + 1).sum()); // 이게 시간 뒤지게 잡아먹음
        arr[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            arr[i] = arr[i - 1] + i;
        } 
        int start = 0;
        int end = 1;

        while (start < n && end < n + 1) {
            if (n == arr[end] - arr[start]) {
                answer += 1;
                end += 1;
            } else if (n > arr[end] - arr[start]) {
                end += 1;
            } else {
                start += 1;
            }
        }
        return answer;
    }
}
