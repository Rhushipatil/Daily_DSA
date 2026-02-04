import java.util.*;
public class operators {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        // System.out.println("enter your prefred number");
        // int a=sc.nextInt();
        // if(a >0){
        //     System.out.println("the number is positive");
        // }
        // else if(a<0){
        //     System.out.println("the number is negative");
        // }
        // else{
        //     System.out.println("the number is zero");
        // }

        /////////////////////////////
        // System.out.println("enter number of the week");
        // int a=sc.nextInt();
        // switch(a){
        //     case 1:
        //     System.out.println("monday");
        //     break;
        //     case 2:
        //     System.out.println("tuesday");      
        //     break;
        //     case 3:
        //     System.out.println("wednesday");
        //     break;

        //     case 4:
        //     System.out.println("thursday");
        //     break;
        //     case 5:
        //     System.out.println("friday");
        //     break;
        //     case 6:
        //     System.out.println("saturday");
        //     break;
        //     case 7:
        //     System.out.println("sunday");
        //     break;
        //     default:
        //     System.out.println("invalid input");
        // }
        ////////////////////////////

        /// year is leap or not
        System.out.println("enter the prefered year");
        int year=sc.nextInt();
        if((year %4==0 && year %100 !=0) || (year %400==0)){
            System.out.println("the year is leap year");
        }
        else{
            System.out.println("the year is not leap year");
        }


    }
}
