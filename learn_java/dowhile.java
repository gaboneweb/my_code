import java.util.Scanner;
/* 
 A do...while loop is similar to a while loop, 
 except that a do...while loop is guaranteed to execute at least one time.
*/

class MyDoWhile {
    public static void main(String[] args){
        int x = 1;
        do {
            System.out.println(x);
            x++;
        } while(x < 5);
        /*This loop will run atleast once as the do block is run
          before the condition is tested

          Condition appears at the end of the loop
        */

        int x1 = 1;
        do {
            System.out.println(x);
            x1++;
        } while(x1 < 0);
        /* In do…while loops:
           the while is just the condition and doesn't have a body itself.
           */

        /* Write a program that will continuously take a password as input and output "Write password",
            until the client inserts the correct password(8819).*/
        Scanner read = new Scanner(System.in);
        int password;
        do{
            System.out.println("Write password");
            password = read.nextInt();
        }while(password != 8819);


    }
}