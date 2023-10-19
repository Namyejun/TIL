// https://school.programmers.co.kr/learn/courses/30/lessons/12949
package CodingTest.Java;

class Solution24 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        for (int i1 = 0; i1 < arr1.length; i1++) {
            for (int j1 = 0; j1 < arr2[0].length; j1++) {
                int temp = 0;
                for (int t = 0; t < arr1[0].length; t++) {
                    temp += arr1[i1][t] * arr2[t][j1];
                }
                answer[i1][j1] = temp;
            }
        }
        return answer;
    }
}

// 43 32 -> 42

// 00 01 02  00 01
// 10 11 12  10 11
// 20 21 22  20 21
// 30 31 32