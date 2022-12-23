class MyClass {
    public static void main(String [ ] args){

        /*Pre-increment also known as Prefix  */
        int test = 5;
        ++test;// test is now 6
        System.out.println(test);

        int test1 = 5;
        --test1;// test is now 6
        System.out.println(test1);

        /*Post-increment also know as Postfix */
        int test2 = 5;
        
        System.out.println(test2++);// test2 is still 5
        System.out.println(test2);//Now test2 is now 6

        int test3 = 5;
        System.out.println(test3--);// test3 is still 5
        System.out.println(test3);//Now test2 is now 4

    }
}