// https://school.programmers.co.kr/learn/courses/30/lessons/17680
package CodingTest.Java;

import java.util.LinkedList;
import java.util.Queue;

public class Solution25 {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        // List<String> cache = new ArrayList<>(cacheSize);
        Queue<String> cache = new LinkedList<>();
        for (int i = 0; i < cities.length; i++) {
            String city = cities[i].toLowerCase();
            if (cacheSize > 0) {
                if (cache.contains(city)) {
                    cache.remove(city);
                    cache.add(city);
                    answer += 1;
                } else {
                    if (cache.size() >= cacheSize) {
                        cache.remove();
                    }
                    cache.add(city);
                    answer += 5;
                }
            } else {
                answer = cities.length * 5;
            }
        }
        return answer;
    }
}
