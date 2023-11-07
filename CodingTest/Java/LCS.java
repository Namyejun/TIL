package CodingTest.Java;

public class LCS {
    public static void main(String[] args) {
        LCS lcs = new LCS();
        System.out.println(lcs.longestCommonSubstring("ABCDEF", "GBCDFE"));
        System.out.println(lcs.longestCommonSubsequence("ABCDEF", "GBCDFE"));
    }

    // 최장 공통 문자열
    public int longestCommonSubstring(String s1, String s2) {
        int answer = -1;

        int[][] lcs = new int[s1.length() + 1][s2.length() + 1];
        
        for (int i = 0; i < lcs.length; i++) {
            for (int j = 0; j < lcs[i].length; j++) {
                if (i == 0 || j == 0) {
                    lcs[i][j] = 0;
                } else if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                }
                if (lcs[i][j] > answer) answer = lcs[i][j];
            }
        }
        return answer;
    }

    // 최장 공통 부분 문자열
    public int longestCommonSubsequence(String s1, String s2) {
        int answer = -1;

        int[][] lcs = new int[s1.length() + 1][s2.length() + 1];
        
        for (int i = 0; i < lcs.length; i++) {
            for (int j = 0; j < lcs[i].length; j++) {
                if (i == 0 || j == 0) {
                    lcs[i][j] = 0;
                } else if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                } else {
                    lcs[i][j] = Math.max(lcs[i-1][j], lcs[i][j-1]);
                }
                if (lcs[i][j] > answer) answer = lcs[i][j];
            }
        }
        return answer;
    }
}
