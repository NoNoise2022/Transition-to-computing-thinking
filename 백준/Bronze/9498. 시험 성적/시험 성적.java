import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        //
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        if (a>=90) {
            System.out.println("A");
        } else if (a>=80) {
            System.out.println("B");
        } else if (a>=70) {
            System.out.println("C");
        } else if (a>=60) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }



/*
        String str = "";

        if (a<=100) {
            str = "A";
            if (a<90) {
                str = "B";
                if (a<80) {
                    str = "C";
                    if (a<70) {
                        str = "D";
//                        System.out.println("D");
                    } else {
                        str = "F";

//                        System.out.println("F");
                    }
//                    System.out.println("C");
                }
//                System.out.println("B");
            }
//            System.out.println("A");
        }
        System.out.println(str);
*/
        /*
                if (a<=100) {
            System.out.println("A");
        } else if (a<90) {
            System.out.println("B");
        } else if (a<80) {
            System.out.println("C");
        } else if (a<70) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }


                if (a>60) {
            System.out.println("A");
        } else if (a>70) {
            System.out.println("B");
        } else if (a>80) {
            System.out.println("C");
        } else if (a>90) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }

         */
    }
}
