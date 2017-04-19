
public class SmaNum {
	public static void main (String[] args) {
		//System.out.println("\nresult = [ " + result + " ]\n");

		int n = 10;
		boolean run = true;

		while (run) {
			if (n % 3 == 0) {
				if (n % 4 == 0) {
					if (n % 6 == 0) {
						if (n % 7 == 0) {
							if (n % 8 == 0) {
								if (n % 9 == 0) {
									if (n % 10 == 0) {
										if (n % 11 == 0) {
											if (n % 12 == 0) {
												if (n % 13 == 0) {
													if (n % 14 == 0) {
														if (n % 15 == 0) {
															if (n % 16 == 0) {
																if (n % 17 == 0) {
																	if (n % 18 == 0) {
																		if (n % 19 == 0) {
																			System.out.println("\nn = [ " + n + " ]\n");
																			run = false;
																			break;
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
			n += 10;
		}
		//System.out.println("\nn = [ " + n + " ]\n");
	}
}