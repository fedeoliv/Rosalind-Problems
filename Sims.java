// http://rosalind.info/problems/sims/

import java.util.*;

public class Sims {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        char[] c = sc.next().toCharArray();
        char[] d = sc.next().toCharArray();
        int[][] dp = new int[c.length + 1][d.length + 1];
        
        for (int i = 0; i <= c.length; i++) {
            for (int j = 1; j <= d.length; j++) {
                int ans = Integer.MIN_VALUE;
                
                if (i > 0) 
                	ans = Math.max(ans, dp[i - 1][j] - 1);
                
                if (j > 0) 
                	ans = Math.max(ans, dp[i][j - 1] - 1);
                if (i > 0 && j > 0) {
                    if (c[i - 1] == d[j - 1]) 
                    	ans = Math.max(ans, dp[i - 1][j - 1] + 1); 
                    else
                    	ans = Math.max(ans, dp[i - 1][j - 1] - 1);
                }
                
                dp[i][j] = ans;
            }
        }        
        
        int score = Integer.MIN_VALUE;
        int bi = -1;
        int bj = -1;
        
        for (int i = 0; i <= c.length; i++) {
            for (int j = 0; j <= d.length; j++) {
                if (j < d.length) 
                	continue;
                
                if (score < dp[i][j]) {
                    score = dp[i][j];
                    bi = i;
                    bj = j;
                }
            }
        }
        
        System.out.println(score);
        
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        
        for (; bj > 0;) {
            if (bi > 0 && dp[bi - 1][bj] - 1 == dp[bi][bj]) {
                s1.append(c[bi - 1]);
                s2.append('-');
                --bi;   
            } else if (bj > 0 && dp[bi][bj - 1] - 1 == dp[bi][bj]) {
                s1.append('-');
                s2.append(d[bj - 1]);
                --bj;
            } else {
                s1.append(c[bi - 1]);
                s2.append(d[bj - 1]);
                --bi;
                --bj;
            }
        }
        
        System.out.println(s1.reverse());
        System.out.println(s2.reverse());
    }
}
