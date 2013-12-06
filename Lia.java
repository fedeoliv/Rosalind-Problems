// http://rosalind.info/problems/lia/

public class Lia {
	private static double getProbability(int k, int n) {
		int children = (int) Math.pow(2, k);
		
		return 1 - prob(n - 1, 0.25, children);
	}
	
	private static double prob(int s, double p, int n) {
		double x = 1.0 - p;
		int a = n - s;
		int b = s + 1;
		int c = a + b - 1;
		
		double result = 0;
		
		for(int i = a; i < c + 1; i++)
			result += factorial(c) / (factorial(i) * factorial(c - i)) * Math.pow(x, i) * Math.pow(1 - x, c - i);
		
		return result;
	}
	
	private static double factorial(int n) {
		int result = 1;
		
		for(int i = 2; i <= n; i++) {   
		     result *= i;  
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(getProbability(2, 1));
	}
}
