import java.util.Scanner;
/*for loop syntax
 *for (initialization; condition; increment/decrement) {
   statement(s)
  }
 * Initialization: Expression executes only once during the beginning of loop
 * Condition: Is evaluated each time the loop iterates. The loop executes the
   statement repeatedly, until this condition returns false.
 * Increment/Decrement: Executes after each iteration of the loop.
 */


class MyForLoops {
    /**
     * @param args
     */
    public static void main(String [] args){
        /* A for loop allows you to efficiently write a loop that needs to execute 
           a specific number of times.
         */
        

        //For loop that runs 5 times
        for(int x = 1; x<=5 ; x++){
            System.out.println(x);
        }

        /*
         * Complete the program to calculate the factorial of the given 
            number and output it.
        */
        Scanner scanner = new Scanner(System.in);
        int  number = scanner.nextInt();
        int fact = 1;
        //your code goes here
        for (int i = number; i > 0; i--){
            fact *= i;
        }
        System.out.println(fact);
        
      
        int n = scanner.nextInt();  
        for(int j = 1; j <= n; j++){
           System.out.println("Welcome");
        }
        scanner.close();

        /*You can any type of condition
         * You can also have any kind of increment statements in the for loop
         * 
         * The example code below prints only the even values between  0 and 10: 
         */

         for(int x = 0; x <=10; x=x+2){
            System.out.println(x);
         }

         /*A for loop is the best when the  starting and ending numbers are known. */
    }
}