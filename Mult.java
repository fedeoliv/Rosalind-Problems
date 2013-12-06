// http://rosalind.info/problems/mult/

import java.util.*;

public class Mult {

    static int[] count;
    
    static int cost(char[] d) {
        if (count == null) count = new int[5];
        Arrays.fill(count, 0);
        for (char e : d) count["ACGT-".indexOf(e)]++;
        int ans = 0;
        for (int i : count) ans += i * (d.length - i);
        return ans >> 1;
    }
    
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        
		Scanner sc = new Scanner(System.in);
        int n = 4;
        char[][] c = new char[n][];
        int[] delta = new int[n];
        int[] z = new int[n];
        char[] d = new char[n];
        int states = 1;
        
        for (int i = 0; i < n; i++) 
        	c[i] = sc.next().toCharArray();
        
        for (int i = 0; i < n; i++) {
            delta[i] = states;
            states *= c[i].length + 1;
        }
        
        int[] dp = new int[states];
        
        for (int i = 0; i < states; i++) {
            if (i == 0) {
                dp[i] = 0;
                continue;
            }
            
            int ans = Integer.MIN_VALUE;
            
            for (int j = 0; j < n; j++)
            	z[j] = i / delta[j] % (c[j].length + 1);
            
            for (int mask = 1; mask < 1 << n; mask++) {
                boolean ok = true;
                int ni = i;
                
                for (int j = 0; j < n; j++) {
                    if (((mask >> j) & 1) == 1) {
                        if (z[j] == 0) {
                            ok = false;
                            break;
                        }
                        
                        d[j] = c[j][z[j] - 1];
                        ni -= delta[j];
                    } else {
                        d[j] = '-';
                    }
                }
                
                if (!ok) 
                	continue;
                
                ans = Math.max(ans, dp[ni] - cost(d));
            }
            
            dp[i] = ans;
        }
        
        System.out.println(dp[states - 1]);
        
        StringBuilder[] ans = new StringBuilder[n];
        
        for (int i = 0; i < n; i++) ans[i] = new StringBuilder();
        all: for (int i = states - 1; i > 0; ) {
            for (int j = 0; j < n; j++) 
            	z[j] = i / delta[j] % (c[j].length + 1);
            
            for (int mask = 1; mask < 1 << n; mask++) {
                boolean ok = true;
                int ni = i;
                
                for (int j = 0; j < n; j++) {
                    if (((mask >> j) & 1) == 1) {
                        if (z[j] == 0) {
                            ok = false;
                            break;
                        }
                        
                        d[j] = c[j][z[j] - 1];
                        ni -= delta[j];
                    } else {
                        d[j] = '-';
                    }
                }
                
                if (!ok) 
                	continue;
                
                if (dp[i] == dp[ni] - cost(d)) {
                    i = ni;
                    
                    for (int j = 0; j < n; j++) 
                    	ans[j].append(d[j]); 
                    
                    continue all;
                }
            }
            
            throw new AssertionError();            
        }
        
        for (StringBuilder a : ans) {
            System.out.println(a.reverse());
        }
    }
}
