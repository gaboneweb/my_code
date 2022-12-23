/*
 * JAVA ARITHMETIC OPERATORS
 * + addition
 * - subtraction
 * * multiplication
 * / division
 * % modulo
 */

 class MyClassMath {
    public static void main(String [] args){
        //addition
        int sum1 = 50 + 10;
        int sum2 = sum1 + 66;
        int sum3 = sum2 + sum1;

        //Subtraction
        int sum4 = 1000 + 10;
        int sum5 = sum4 - 66;
        int sum6 = sum4 - sum5;

        //Multiplication
        int sum7 = 1000 * 2;
        int sum8 = sum7 * 10;
        int sum9 = sum7 * sum8;

        //Division
        int sum10 = 1000 / 5;
        int sum12 = sum10 / 2;
        int sum13 = sum10 / sum12;

        //Modulo
        int value = 23;
        int res = value % 6;// res is 5

        int all_stuff = sum3 + sum6 + sum9 + sum13 + res;

        System.out.println(all_stuff);
    }
 }