
public class NewPrime {
	public static void main (String[] args) {
		//System.out.println("\nresult = [ " + result + " ]\n");

		int result = getPrime(10001);
		System.out.println("\nresult = [ " + result + " ]\n");
	}

	public static int getPrime(int level) {

		int n = 11;
		int count = 4;
		while (count < level) {
			if (isPrime(n)) {
				count += 1;
			}
			n += 2;
		}
		n -= 2;
		return n;
	}

	public static boolean isPrime(int n) {
    //check if n is a multiple of 2
    if (n%2 == 0) return false;
    //if not, then just check the odds
    for(double i=3; i*i <= n; i+=2) {
      if(n%i == 0) {
        return false;
      }
    }
    return true;
	}
}