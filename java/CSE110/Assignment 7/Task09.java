import static java.lang.System.*;
import java.util.*;
public class Task09 { 
    public static void main (String[] args) {
        Scanner sc = new Scanner(in);
    
        out.println("Enter the quantity of students");
        int q = sc.nextInt();
        
        int []ID= new int[8];
        String []name= new String[q];
        int []mark= new int[1];
        
        for(int n=0;n<q;n++)
        {
            out.println("Please enter student's name");
            name [n] = sc.nextLine(); 
           
            out.println("Please enter student's ID");
            ID [n] = sc.nextInt();
            
            out.println("Please enter student's mark");
            mark [n] = sc.nextInt();
        }
        
        
        for (int m=0; m < q; m++) {
            out.print(name[m]+" ");
            out.print(ID[m]+" ");
            out.print(mark[m]+" ");
        }
    }
}