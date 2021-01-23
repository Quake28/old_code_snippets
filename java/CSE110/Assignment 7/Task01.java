import static java.lang.System.*;
import java.util.*;
public class Task01 { 
    public static void main (String[] args) {
        Scanner sc = new Scanner(in);
        //START
        
        int[] marks = new int[] {10, 30, 20, 50,40};  
        int total = 0;
        int highest = marks[0];
        int lowest = marks[0];
        for(int count=0;count<marks.length;count++){
            if (highest<marks[count]) {
                highest = marks[count];
            }
            else if (lowest>marks[count]) {
                lowest = marks[count];
            }
            total += marks[count];
        }
        int average = total / marks.length;
        out.println("Highest mark is "+highest);
        out.println("Lowest mark is "+lowest);
        out.println("Average mark is "+average);
        
        //END
        sc.close();
    }
}