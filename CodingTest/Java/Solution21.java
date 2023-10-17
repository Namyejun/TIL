// https://school.programmers.co.kr/learn/courses/30/lessons/76502
package CodingTest.Java;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Solution21 {
    public int solution(String s) {
        int answer = 0;
        String[] s2 = s.split("");
        Queue<String> queue = new LinkedList<>();
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            queue.add(s2[i]);
        }
        for (int i = 0; i < s.length(); i++) {
            Iterator<String> iter = queue.iterator();
            while (iter.hasNext()) {
                String s3 = iter.next();
                if (!stack.empty() && chk(stack.peek(), s3)) {
                    stack.pop();
                } else {
                    stack.push(s3);
                }
            }

            if (stack.empty()) {
                answer += 1;
            }

            queue.add(queue.remove());
            stack.clear();
        }

        return answer;
    }

    public boolean chk(String peek, String s3) {
        if (s3.equals("]")) {
            if (peek.equals("[")){
                return true;
            } else {
                return false;
            }
        } else if (s3.equals("}")) {
            if (peek.equals("{")){
                return true;
            } else {
                return false;
            }
        } else if (s3.equals(")")) {
            if (peek.equals("(")){
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}
