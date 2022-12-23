
/*
 * Code for learning Java conditionals
 */

 class MyConditionals {
        public static void main(String[ ] args){

        /*if...else statements */
        int age = 30;
        if(age < 16){
            System.out.println("Too young");
        }else {
            System.out.println("Welcome!");
        }

        /*else if statements */
        int age1 = 25;
        if(age1 <= 0) {
            System.out.println("Error");
        } else if(age1 <= 16) {
            System.out.println("Too Young");
        } else if(age1 < 100) {
            System.out.println("Welcome!");
        } else {
            System.out.println("Really?");
        }

        /*Nested  if...else statement*/

        int age2 = 25;
        if(age2 > 0){
            if(age2 > 16){
                System.out.println("Weclome!");
            }else {
                System.out.println("Too Young!");
            }
        }else {
            System.out.println("Error");
        }
    }
 }



