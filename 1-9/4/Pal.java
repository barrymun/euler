
public class Pal {
	public static void main (String[] args) {

		int val = 999;
		int result = 0;

		//System.out.println("\nisPal = [ " + isPal(12021) + " ]\n");

		while (val > 1) {
			for (int i = 999; i > 1; i-=1) {
				// System.out.println("\ni = [ " + i + " ]\n");
				// System.out.println("\ni*val = [ " + i*val + " ]\n");
				// break;
				if (isPal(i*val)) {
					if (i*val > result) {
						result = i*val;
					}
				}
			}
			val -= 1;
		}
		System.out.println("\nresult = [ " + result + " ]\n");
	}

	public static boolean isPal(int n) {
		int temp = n;
		int result = 0;
		while (temp > 0) {
			result += temp % 10;
			if (temp / 10 > 0) {
				result *= 10;
			}
			temp /= 10;
		}

		if (result == n) {
			return true;
		}
		return false;
	}
}