
import java.util.Scanner;

class fibonacciIterative {
    static int fib(int n) {
        if(n<=1){
            return n;
        }
        return fib(n-1)+fib(n-2);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number");
        int n =sc.nextInt();

        System.out.println("recursive fibonacci series");
                for(int i=0; i<n;i++){
                    System.out.print(fib(i) + " ");
                }
    }
}
