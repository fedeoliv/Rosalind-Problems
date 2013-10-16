import javax.swing.JOptionPane;

/* Problem ID: FIB
 * http://rosalind.info/problems/fib/
 */

public class Fib {
	public static void main(String[] args) {
		int n = Integer.parseInt(JOptionPane.showInputDialog(null));
		int k = Integer.parseInt(JOptionPane.showInputDialog(null));
		
		int[] rabbits = new int[n];
		
		/*Using the Fibonacci sequence, but we multiply 
		  the previous generation by k.
		*/
		
	    for(int i = 0; i < n; i++) {
	        if (i == 0 || i == 1) {
	        	rabbits[i] = 1;
	        } else {
	        	rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2];
	        }
	    }
	    
		System.out.println(rabbits[n-1]);
	}
}
