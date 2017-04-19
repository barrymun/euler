
public class Mul {
	public static void main (String[] args) {
		int result1 = cal(3);
		int result2 = calfive(5);
		int total = result1 + result2;
		System.out.println("\nTotal = [ " + total + " ]\n");
	}

	public static int cal(int n) {
		int result = 0;
		int i = 1;
		while (n*i < 1000) {
			// System.out.println("\nresult = [ " + n*i + " ]\n");
			result += n*i;
			i += 1;
		}
		return result;
	}

	public static int calfive(int n) {
		int result = 0;
		int i = 1;
		while (n*i < 1000) {
			// System.out.println("\nresult = [ " + n*i + " ]\n");
			if (n*i % 3 != 0) {
				result += n*i;
			}
			i += 1;
		}
		return result;
	}
}