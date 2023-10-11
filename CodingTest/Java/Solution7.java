// https://school.programmers.co.kr/learn/courses/30/lessons/181187
package CodingTest.Java;

class Solution7 {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for (int i = 1; i <= r2; i++) {
            long minJ = (int) Math.ceil(Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2)));
            long maxJ = (int) Math.floor(Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2)));
                
            answer = answer + (maxJ - minJ) + 1;
        }
        
        return answer * 4;
    }
}

// 4,5,6,7,8,9
// 2,2,0,0,2,2