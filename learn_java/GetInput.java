import java.util.Scanner;// Import the Scanner class to use the Scanner object.


class MyClassInput {
    public static void main(String[ ] args) {
        Scanner myVar = new Scanner(System.in);
        System.out.println(myVar.nextLine());    
        System.out.println(myVar.nextInt());
        
        myVar.close();
    }
}

/*
 * Read a byte - nextByte()
 * Read a short - nextShort()
 * Read an int - nextInt()
 * Read a long - nextLong()
 * Read a float - nextFloat()
 * Read a double - nextDouble()
 * Read a boolean - nextBoolean()
 * Read a complete line - nextLine()
 * Read a word - next() 
 */