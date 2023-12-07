// https://school.programmers.co.kr/learn/courses/30/lessons/150369
package CodingTest.Java;

public class Solution33 {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int idx = n - 1;
        int deliveryCapacity = 0;
        int pickupCapacity = 0;

        for (int i = idx; i >= 0; i--) {
            if (deliveries[i] != 0 || pickups[i] != 0) {
                int count = 0;
                
                while (deliveryCapacity < deliveries[i] || pickupCapacity < pickups[i]) {
                    deliveryCapacity += cap;
                    pickupCapacity += cap;
                    count += 1;
                }

                deliveryCapacity -= deliveries[i];
                pickupCapacity -= pickups[i];

                answer += ((i + 1)*count*2);
            }
        }

        return answer;
    }
}
