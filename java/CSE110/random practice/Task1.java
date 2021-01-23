import static java.lang.System.*;
import java.util.*;

public class Task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(in);
        out.print("Please enter the quantity of numbers: ");
        int quantity = sc.nextInt();
        int product = 1;
        for(int count=0; count<quantity;count++) {
            out.print("Please enter a number");
            product*=sc.nextInt();
        }
        out.println(product);
    }
}