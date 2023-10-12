// https://school.programmers.co.kr/learn/courses/30/lessons/12911
package CodingTest.Java;

public class Solution10 {
    public int solution(int n) {
        int answer = 0;
        String binN = Integer.toBinaryString(n);
        int nn = n + (int) Math.pow(2, binN.length() - binN.lastIndexOf("1") - 1);
        String binNN = Integer.toBinaryString(nn);
        int nCnt = binN.length() - binN.replace("1", "").length();
        int nnCnt = binNN.length() - binNN.replace("1", "").length();

        int diff = nCnt - nnCnt;
        
        answer = nn + (int) Math.pow(2, diff) - 1;

        return answer;
    }
}


