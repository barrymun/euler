
public class Trip {
	public static void main (String[] args) {
		//System.out.println("\nresult = [ " + result + " ]\n");

		int result = getProduct();
		System.out.println("\nresult = [ " + result + " ]\n");
	}

	public static int getProduct() {
		int i,j,k;
		int result = 0;
		for (i=1; i<=1000; i++) {
			for (j=1; j<=1000; j++) {
				for (k=1; k<=1000; k++) {
					if (i+j+k == 1000) {
						if (i*i + j*j == k*k || i*i + k*k == j*j || j*j + k*k == i*i) {
							result = i*j*k;
							break;
						}
					}
				}
				k=1;
			}
			j=1;
		}
		return result;
	}
}