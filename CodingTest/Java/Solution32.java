// https://school.programmers.co.kr/learn/courses/30/lessons/150368
package CodingTest.Java;

public class Solution32 {
    int emoticonPlus = 0;
    int soldAmount = 0;

    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = {0, 0};
        
        int[] arr = new int[emoticons.length];
        combination(arr, 0, users, emoticons);

        answer[0] = emoticonPlus;
        answer[1] = soldAmount;
        return answer;
    }

    public void calc(int[] arr, int[][] users, int[] emoticons) {
        int localEmoticonPlus = 0;
        int localSoldAmount = 0;
        
        for (int i = 0; i < users.length; i++) {
            int amount = 0;
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] >= users[i][0]) { // 할인율이 더 쎈경우 산다.
                    amount += emoticons[j] * (100 - arr[j]) / 100;
                }
            }

            if (amount >= users[i][1]) {
                localEmoticonPlus += 1;
            } else {
                localSoldAmount += amount;
            }
        }

        if (localEmoticonPlus > emoticonPlus) {
            emoticonPlus = localEmoticonPlus;
            soldAmount = localSoldAmount;
        } else if (localEmoticonPlus == emoticonPlus) {
            if (localSoldAmount > soldAmount) {
                soldAmount = localSoldAmount;
            }
        }
    }

    public void combination(int[] arr, int index, int[][] users, int[] emoticons) {
        if (index == arr.length) {
            calc(arr, users, emoticons);
            return;
        }

        for (int i = 10; i <= 40; i += 10) {
            arr[index] = i;
            combination(arr, index + 1, users, emoticons);
        }
    }
}
