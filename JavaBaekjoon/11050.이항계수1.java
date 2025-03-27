import java.util.Scanner;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

// 이항계수1
public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();

		System.out.println(factorial(n) / (factorial(n-k) * factorial(k)));

	}

	private static int factorial(int n) {
		if(n <= 1) return 1;
		else return n * factorial(n-1);
	}
}