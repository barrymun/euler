
public class Collatz {
	public static void main (String[] args) {
		//System.out.println("\ntotal = [ " + total + " ]\n");

		double val = 999999.0;
		double temp = 0;
		int result = 0;

		while (val > 0.0) {
			if (getChainLength(val) > result) {
				result = getChainLength(val);
				temp = val;
			}
			val -= 1.0;
		}

		System.out.println("\nvalue, Chain Length = [ " + temp + ", " + result + " ]\n");
	}

	public static int getChainLength(double n) {
		int cLen = 1;
		while (n > 1.0) {
			if (n % 2.0 == 0.0) {
				n /= 2.0;				
			} else {
				n *= 3.0;
				n += 1.0;
			}
			cLen += 1;
		}
		return cLen;
	}

}
