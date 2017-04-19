
public class Square {
	public static void main (String[] args) {
		//System.out.println("\nresult = [ " + result + " ]\n");

		int resultA = squareIndiv();
		int resultB = addAndSquare();
		int total = resultB - resultA;
		System.out.println("\ntotal = [ " + total + " ]\n");
	}

	public static int squareIndiv() {
		int result = 0;
		for (int i = 1; i <= 100; i++) {
			result += i*i;
		}
		return result;
	}

	public static int addAndSquare() {
		int result = 0;
		for (int i = 1; i <= 100; i++) {
			result += i;
		}
		result *= result;
		return result;
	}
}