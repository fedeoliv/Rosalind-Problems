// http://rosalind.info/problems/ctea/

public class Ctea {
	private static final int MODULO = 134_217_727;
	
	public static int getOpticalAlignment(char[] s, char[] t) {
        int[][] last = new int[s.length + 1][t.length + 1];
        int[][] alignments = new int[s.length + 1][t.length + 1];
        
        for (int i = 0; i <= s.length; i++) {
            for (int j = 0; j <= t.length; j++) {
                int ans = Integer.MAX_VALUE;
                int cnt = 0;
                
                if (i > 0) {
                    if (last[i - 1][j] + 1 < ans) {
                        cnt = alignments[i - 1][j];
                        ans = last[i - 1][j] + 1;
                    } else if (last[i - 1][j] + 1 == ans) {
                        cnt += alignments[i - 1][j];
                        if (cnt >= MODULO) 
                        	cnt -= MODULO;
                    }
                }
                
                if (j > 0) {
                    if (last[i][j - 1] + 1 < ans) {
                        cnt = alignments[i][j - 1];
                        ans = last[i][j - 1] + 1;
                    } else if (last[i][j - 1] + 1 == ans) {
                        cnt += alignments[i][j - 1];
                        if (cnt >= MODULO) cnt -= MODULO;
                    }
                }
                
                if (i > 0 && j > 0) {
                    int better = s[i - 1] == t[j - 1] ? last[i - 1][j - 1] : last[i - 1][j - 1] + 1;
                    
                    if (better < ans) {
                        ans = better;
                        cnt = alignments[i - 1][j - 1];
                    } else if (better == ans) {
                        cnt += alignments[i - 1][j - 1];
                        if (cnt >= MODULO) cnt -= MODULO;
                    }
                }
                
                if (ans == Integer.MAX_VALUE) {
                    ans = 0;
                    cnt = 1;
                }
                
                last[i][j] = ans;
                alignments[i][j] = cnt;
            }
        }        
        
        return alignments[s.length][t.length];
	}
	
    public static void main(String[] args) {
    	char[] s = "PLEASANTLY".toCharArray();
    	char[] t = "MEANLY".toCharArray();
    	
    	System.out.println(getOpticalAlignment(s, t));
    }
}
