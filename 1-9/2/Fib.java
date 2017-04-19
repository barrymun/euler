
public class Fib {
	public static void main(String[] args) {
		int a = 1;
		int b = 2;
		int c = 0;
		int step = 1;
		int total = 2;

		while (b < 4000000) {
			c = a + b;
			if (step % 3 == 0 && step != 0) {
				if (c < 4000000) {
					total += c;
					System.out.println("\nc = [ " + c + " ]\n");
					step = 0;
				}
			}
			step += 1;
			a = b;
			b = c;
			c = 0;
		}
		System.out.println("\nTotal = [ " + total + " ]\n");
	}
}