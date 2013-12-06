// http://rosalind.info/problems/mgap/

public class Mgap {
    public static void main(String[] args) {
        char[] s = "AACGTA".toCharArray();
        char[] t = "ACACCTA".toCharArray();		
        int[][] dp = new int[s.length + 1][t.length + 1];
        
        for (int i = 0; i <= s.length; i++) {
            for (int j = 0; j <= t.length; j++) {   
                int answer = Integer.MIN_VALUE;
                
                if (i > 0) 
                	answer = Math.max(answer, dp[i - 1][j]);
                
                if (j > 0) 
                	answer = Math.max(answer, dp[i][j - 1]);
                
                if (i > 0 && j > 0 && s[i - 1] == t[j - 1]) 
                	answer = Math.max(answer, dp[i - 1][j - 1] + 1);
                
                if (answer == Integer.MIN_VALUE) 
                	answer = 0;
                
                dp[i][j] = answer;
            }
        }
        
        System.out.println(s.length + t.length - 2 * dp[s.length][t.length]);
    }
}
