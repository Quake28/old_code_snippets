import static java.lang.System.* ;
class Main
{
    public static void main(String[] args)
    {
        double book1 = 7.99;
        double book2 = 8.99;
        double book3 = 9.99;
        double book4 = 12.99;
        out.print("Prices of the book are as follows:\n");
        out.printf("Price Book1 ($): %.2f\n",book1);
        out.printf("Price Book2 ($): %.2f\n",book2);
        out.printf("Price Book3 ($): %.2f\n",book3);
        out.printf("Price Book4 ($): %.2f\n",book4);
        out.printf("===========================\n");
        
        double bookTotal1 = book1+book2;
        out.printf("Total when 2 books are purchased = $ %.2f\n",bookTotal1);
        out.printf("Discount (2 books) = 20%%\n");
        double discount1= bookTotal1*0.8;
        out.printf("Total after Discount = $ %.2f\n",discount1);
        double grandTotal1= discount1*1.12;
        out.printf("Grand total with Tax (12%%) = $ %.2f\n",grandTotal1);
        
        out.printf("===========================\n");

        double bookTotal2 = book1+book2+book3;
        out.printf("Total when 3 books are purchased = $ %.2f\n",bookTotal2);
        out.printf("Discount (3 books) = 30%%\n");
        double discount2= bookTotal2*0.7;
        out.printf("Total after Discount = $ %.2f\n",discount2);
        double grandTotal2= discount2*1.12;
        out.printf("Grand total with Tax (12%%) = $ %.2f\n",grandTotal2);

        out.printf("===========================\n");

        double bookTotal3 = book1+book2+book3+book4;
        out.printf("Total when 4 books are purchased = $ %.2f\n",bookTotal3);
        out.printf("Discount (4 books) = 35%%\n");
        double discount3= bookTotal3*0.65;
        out.printf("Total after Discount = $ %.2f\n",discount3);
        double grandTotal3= discount3*1.12;
        out.printf("Grand total with Tax (12%%) = $ %.2f\n",grandTotal3);
    }
}