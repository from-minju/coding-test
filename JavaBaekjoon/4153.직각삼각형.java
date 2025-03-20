import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

// 4153. 직각삼각형
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(true){

			String str = sc.nextLine();

			if(str.equals("0 0 0")){
				break;
			}

			Integer[] arr = Arrays.stream(str.split(" ")).map(Integer::parseInt).toArray(Integer[]::new);

			Arrays.sort(arr, Collections.reverseOrder());

			if (arr[0]*arr[0] == arr[1]*arr[1] + arr[2]*arr[2]) {
				System.out.println("right");
			} else {
				System.out.println("wrong");
			}

		}

		sc.close();

	}

}