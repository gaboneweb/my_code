/* Logical operators are used to combine multiple conditions. 
 * AND operator (&&)  --> both conditions are true
 * OR operator (||) --> any one of the conditions is true
 * NOT operator (!)  --> reverses the logical state of its operand.
*/

class MyClassLogical {
    public static void main(String [] args){
        int age = 22;
        int money = 800;
        /*Conditionals without the logical operators */
        if (age > 18) {
            if (money > 500) {
                System.out.println("Welcome!");
            }
        }   
        /*Conditionals with logical operators
         * Shorter and cleaner code
         * Using the AND operator
         */
        if (age > 18 && money > 500) {
            System.out.println("Welcome!");
        }

        /*Using the:
         * OR (||) operator
         */
          
        if (age > 18 || money > 500) {
            System.out.println("Welcome!");
        }

        /*Using the:
         * NOT (!) operator
         */
        if(!(age > 18)) {
            System.out.println("Too Young");
        } else {
            System.out.println("Welcome");
        }
        

        


    }
}