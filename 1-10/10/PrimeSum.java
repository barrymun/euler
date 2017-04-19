
public class PrimeSum {
	public static void main (String[] args) {
		//System.out.println("\nresult = [ " + result + " ]\n");

		double result = sumPrime();
		System.out.println("\nresult = [ " + result + " ]\n");
	}

	public static double sumPrime() {
		double result = 2.0;
		for (double i=3; i<2000000.0; i+=2.0) {
			if (isPrime(i)) {
				result += i;
			}
		}
		return result;
	}

	public static boolean isPrime(double n) {
    //check if n is a multiple of 2
    if (n%2.0 == 0) return false;
    //if not, then just check the odds
    for(double i=3.0; i*i <= n; i+=2.0) {
      if(n%i == 0.0) {
        return false;
      }
    }
    return true;
	}
}