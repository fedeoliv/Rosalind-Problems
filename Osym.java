import java.util.*;

public class Osym {
    private static Scanner sc;

	public static void main(String[] args) {
        sc = new Scanner(System.in);
        char[] c = sc.next().toCharArray();
        char[] d = sc.next().toCharArray();
        int n = c.length;
        int m = d.length;
        int[][] dp = new int[n + 1][m + 1];
        int[][] dp2 = new int[n + 1][m + 1];
        
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
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
                
                if (ans == Integer.MIN_VALUE) 
                	ans = 0;
                
                dp[i][j] = ans;
            }
        }
        
        for (int i = n; i >= 0; i--) {
            for (int j = m; j >= 0; j--) {
                int ans = Integer.MIN_VALUE;
                if (i + 1 <= n) 
                	ans = Math.max(ans, dp2[i + 1][j] - 1);
                
                if (j + 1 <= m) 
                	ans = Math.max(ans, dp2[i][j + 1] - 1);
                
                if (i + 1 <= n && j + 1 <= m) {
                    if (c[i] == d[j]) 
                    	ans = Math.max(ans, dp2[i + 1][j + 1] + 1); 
                    else
                        ans = Math.max(ans, dp2[i + 1][j + 1] - 1);
                }
                
                if (ans == Integer.MIN_VALUE) 
                	ans = 0;
                
                dp2[i][j] = ans;
            }
        }
        
        System.out.println(dp[n][m]);
        long ans = 0;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int cur = c[i - 1] == d[j - 1] ? 1 : -1;
                cur += dp[i - 1][j - 1];
                cur += dp2[i][j];
                ans += cur;
            }
        } 
        
        System.out.println(ans);
    }
}
