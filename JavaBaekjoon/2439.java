import java.util.Scanner;

// [백준 2439] 별 찍기 - 2
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=1; i <= n; i++){

            // 공백출력 : n-i개
            for(int j=0; j<(n-i); j++){
                System.out.print(" ");
            }

            // 별 출력 : k개
            for(int k=0; k<i; k++){
                System.out.print("*");
            }

            System.out.println("");
        }

        sc.close();
    }
}