class MyVariables {
    public static void main(String [] args){
        String name = "David";
        int age = 42;
        double score = 15.9;
        char group = 'z';
        boolean online = true;//A type that has only two possible values: true and false

        System.out.println(name);
        System.out.println(age);
        System.out.println(score);
        System.out.println(group);
        System.out.println(online);
    }
}

/* Variables store data for processing.
A variable is given a name (or identifier), such as area, age, height, and the
like. The name uniquely identifies each variable, assigning a value to the 
variable and retrieving the value stored.

Variables have types. Some examples:
- int: for integers (whole numbers) such as 123 and -456
- double: for floating-point or real numbers with optional decimal points and 
          fractional parts in fixed or scientific notations, such as 3.1416, -55.66.
- String: for texts such as "Hello" or "Good Morning!". Text strings are enclosed 
          within double quotes. 
*/


/*IMPORTANT TO NOTE
 * 
 * It is important to note that a variable is associated with a type, and is only capable of storing values of that particular type.
   For example, an int variable can store integer values, such as 123; but it cannot store real numbers, such as 12.34, or texts, such as "Hello".
 */