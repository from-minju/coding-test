import java.util.Scanner;

// [백준 1152] 단어의 개수
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().trim();

        if(input.length() == 0){
            System.out.println(0);
        }else{
            String[] words = input.split(" ");
            System.out.println(words.length);
        }

        sc.close();
    }
}