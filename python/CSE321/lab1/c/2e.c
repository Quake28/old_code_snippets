#include <stdio.h>

void main() {
    char lamePalindrome[10000];
    char domain[9] = "sheba.xyz";
    scanf("%s",lamePalindrome);
    int counter = 0;
    while(lamePalindrome[counter]!='\0') { counter++; }
    counter--;
    //printf("%d\n",counter);
    int counter2 = counter/2;
    int status = 1;
    while (counter2>=0) {
        //printf("%c %d %c %d\n",lamePalindrome[counter2],counter2,lamePalindrome[counter-counter2],counter-counter2);
        if (lamePalindrome[counter2]!=lamePalindrome[counter-counter2]) { status = 0; break;}
        counter2--;
    }
    if (status) { printf("Palindrome\n"); }
    else { printf("Not Palindrome\n"); }
}