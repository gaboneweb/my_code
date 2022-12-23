import java.util.Scanner;
/*
 * switch (expression) {

   case value1 :

     //Statements

     break; //optional

   case value2 :

     //Statements

     break; //optional

    //You can have any number of case statements.

    default : //Optional

       //Statements

}
 */
class MyClassSwitch {
    public static void main(String [] args){
       Scanner scanner = new Scanner(System.in);
       int emotion = scanner.nextInt();
       /*
       1 - "You are happy!"
       2 - "You are sad!"
       3 - "You are angry!"
       4 - "You are surprised!"
       other - "Unknown emotion."
       */
        switch(emotion) {
            case 1:
                System.out.println("You are happy!");
                break;
            case 2:
                System.out.println("You are sad!");
                break;
            case 3:
                System.out.println("You are angry!");
                break;
            case 4:
                System.out.println("You are surprised!");
            default:
                System.out.println("Unknown emotion."); 
      
            /* 
             * A switch statement can have an optional default case. 
             * The default case can be used for performing a task when none of the cases is matched.
             * NB!! No break is needed in the default case, as it is always the last statement in the switch. 

            */


            
                
        } 
        /*THE SWITCH EXPRESSION*/

        int day = 2;
        String dayType  = switch(day) {
            case 1, 2, 3, 4, 5 -> "Working day";
            case 6, 7 -> "Weekend";
            default -> "Invalid day";
            };
        System.out.println(dayType);
        scanner.close();

        /* The switch expression makes the switch-case block much shorter and doesn't use a break statement. 
         * Notice the -> shorthand after the cases.
        */
    }
 }