import java.util.Scanner;

public class SYGWithCom {
    public static Object calc(int num) {
        if(num > 10) {
            int a = num / 10;
            int b = num % 10;
            if(a % 3 == 0 || b % 3 == 0 || num%3 == 0) {
                return "XX";
            } else {
                return num;
            }
        } else {
            if(num % 3 == 0) {
                return "X";
            } else {
                return num;
            }
        }
    }

    public static void main(String[] args) {
        int num = 1;
        Scanner scanner = new Scanner(System.in);
        while(num <= 40) {
            Object result = calc(num);
            if(num % 2 == 1) { // 컴퓨터 차례
                System.out.println("컴퓨터 : " + result);
            } else { // 사용자 차례
                System.out.print("나 : ");
                String k = scanner.nextLine();
                if(result instanceof Integer) {
                    try {
                        int t = Integer.parseInt(k);
                        if(t != (int) result) {
                            System.out.println("컴퓨터 승!");
                            break;
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("컴퓨터 승!");
                        break;
                    }
                } else if(!result.equals(k)) {
                    System.out.println("컴퓨터 승!");
                    break;
                }
            }
            if(num == 40) {
                System.out.println("무승부!");
            }
            num++;
        }
        System.out.println("게임종료");
    }
}
