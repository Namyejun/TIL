// https://school.programmers.co.kr/learn/courses/30/lessons/12973
package CodingTest.Java;

import java.util.Stack;

class Solution12 {
    public int solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (stack.empty()) {
                stack.push(s.charAt(i));
            } else {
                if (stack.peek().equals(s.charAt(i))) {
                    stack.pop();
                } else {
                    stack.push(s.charAt(i));
                }
            }
        }
        if (stack.empty()) {
            return 1;
        } else {
            return 0;
        }
    }
}