import java.lang.Math;
import java.util.ArrayList;

public class Prime {

	public static final double TEST = 600851475143.0;

	public static void main (String[] args) {
		System.out.println("\nresult = [ " + factor(TEST) + " ]\n");
	}

	public static double factor(double n) {

		double result = 0.0;

		if (isDivisible(n, 2.0)) {
			if (isPrime(n/2.0)) {
				return 2.0;
			}
		}

		for (double i=3.0; i < n; i+=2.0) {
      if (isDivisible(n, i)) {      	
				if (isPrime(i)) {
					System.out.println("\ni= [ " + i + " ]\n");
					result = i;
				}
			}
    }
    return result;

	}

	public static boolean isDivisible(double a, double b) {
		if (a % b == 0.0) {
			return true;
		}
		return false;
	}

	public static boolean isPrime(double n) {
    if (n % 2.0 == 0.0) { return false; }
    for (double i=3.0; i*i <= n; i+=2.0) {
      if (n % i == 0.0) {
        return false;
      }
    }
    return true;
	}

}