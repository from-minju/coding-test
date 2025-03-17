import java.util.Scanner;
import java.util.Arrays;

// [백준 10989] 수 정렬하기 3
public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n];

		// 입력받기
		for (int i=0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		Arrays.sort(arr);

		for(int i=0; i < n; i++) {
			System.out.println(arr[i]);
		}

	}
}