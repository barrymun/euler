
public class Tri {
	public static void main (String[] args) {

		int var = 2200;
		int result = 0;
		int total = 0;

		long before = System.currentTimeMillis();
		while (result < 500) {
			result = getNumDiv(var);
			var += 1;
		}
		total = getTri(var-1);
		long after = System.currentTimeMillis();
		long runTime = after-before;
		System.out.println("\nTime = [ " + runTime + " ms ]\n");

		System.out.println("\nresult = [ " + total + " ]\n");
	}

	public static int getNumDiv(int n) {
		int count = 0;
		int limit = getTri(n);
		for (int i = 1; i <= limit; i++) {
			if (isDivisible(limit, i)) {
				//System.out.println("\ni = [ " + i + " ]\n");
				count += 1;
			}
		}
		return count;
	}

	public static boolean isDivisible(int a, int b) {
		if (a % b == 0) {
			return true;
		}
		return false;
	}

	public static int getTri(int n) {
		int total = 0;
		for (int i=1; i<=n; i++) {
			total += i;
		}
		//System.out.println("\ntotal = [ " + total + " ]\n");
		return total;
	}

}
