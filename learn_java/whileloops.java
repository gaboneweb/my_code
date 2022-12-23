import java.util.Scanner;

class MyWhileLoops {
    public static void main(String [] args){
        /*A while loop statement repeatedly executes a target statement as
          long as a given condition is true
         */

        int x = 3;
        while(x > 0){
            System.out.println(x);
            x--;
        }

        /*
         * Complete the program to calculate the factorial of the given 
            number and output it.
        */
        Scanner scanner = new Scanner(System.in);
        int  number = scanner.nextInt();
        int fact = 1;
        //your code goes here
        while(number > 0 ){
            fact *= number;
            number--;
        }
        System.out.println(fact);
        scanner.close();
    }
}