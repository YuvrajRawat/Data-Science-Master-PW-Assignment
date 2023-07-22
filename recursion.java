import java.util.Scanner;

public class recursion{

    static void printInc(int n){

        if (n == 1){
            System.out.print(n+" ");
            return;
        }

        printInc(n-1);
        System.out.print(n+" ");
    }

    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printInc(n);
        for (int i=0;i<=n;i++){
            
            System.out.println(" "+ i+(i-1)+" ");

        
        }
    }
}