import java.util.Scanner;
import java.util.Arrays;

// [백준 10809] 알파벳 찾기
public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String s = sc.next();
		int[] positions = new int[26]; // 알파벳 소문자는 26개
		Arrays.fill(positions, -1); // 배열 모든 값 -1로 초기화하기

		for (int i=0; i < s.length(); i++) {
			char ch = s.charAt(i);
			int loc = ch - 'a';

			if(positions[loc] == -1){
				positions[loc] = i;
			}
		}

		// 띄어쓰기해서 출력하기
		for (int i=0; i < positions.length; i++) {
			System.out.print(positions[i] + " ");
		}

	}
}