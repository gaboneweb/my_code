/*
 * A String is an object that represents a sequence of characters. 
 * For example, "Hello" is a string of 5 characters. 
 */

 class MyClassString {
    public static void main(String [ ]  args){
        String s = "Hello!";

        /*
         * You are allowed to define an empty string.
         * For example:
         * String str = "";
         */
        System.out.println(s);

        /*
         * The + (plus) operator between strings adds them together to make a new string.
         * This process is called concatenation
         */

        String firstName, lastName;

        firstName = "Bulelani";
        lastName = "Gabonewe";

        System.out.println("My name is " + firstName +" "+lastName);
    }
 }