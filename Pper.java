// http://rosalind.info/problems/pper/

import javax.swing.JOptionPane;

public class Pper {
	public static int MAX_VALUE = 1000000;
	
	private static int getPermutations(int n, int k) {
		/*
		 * Here we have a common permutation.
		 * The only difference is that we need to get the module, if the result
		 * is bigger than the max value (in this case, bigger than 1000000).
		 */
		int total = 1;
		
		for(int i = 0; i < k; i++) {
			total *= (n - i);
			
			if(total > MAX_VALUE)
				total %= MAX_VALUE;
		}
		
		return total;
	}
	
	public static void main(String[] args) {
		int n = Integer.parseInt(JOptionPane.showInputDialog("N:"));
		int k = Integer.parseInt(JOptionPane.showInputDialog("K:"));
		
		JOptionPane.showMessageDialog(null, getPermutations(n, k));
	}
}
