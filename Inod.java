import javax.swing.JOptionPane;

// http://rosalind.info/problems/inod/

public class Inod {
	public static void main(String[] args) {
		int n = Integer.parseInt(JOptionPane.showInputDialog("N:"));
		
		/*
		 * For 'n' leaves (in this case, the leaves are species), 
		 * we have n-2 ancestors. This is one of the concepts of graphs.
		 */
		JOptionPane.showMessageDialog(null, n - 2);
	}
}
