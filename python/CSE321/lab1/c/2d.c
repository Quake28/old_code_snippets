#include <stdio.h>

void main() {
    char lameEmail[10000];
    char domain[9] = "sheba.xyz";
    scanf("%s",lameEmail);
    //printf("%s\n",lameEmail);
    int counter = 0;
    while(lameEmail[counter]!='@') { counter++; }
    counter++;
    int counter2 = counter;
    while(lameEmail[counter2]!='\0') { counter2++; }
    int counter3 = counter;
    int status = 1;
    while (counter3!=counter2)
    {
        // printf("%c %c\n",lameEmail[counter3],domain[counter3-counter]);
        if (lameEmail[counter3]!=domain[counter3-counter]) { status = 0; break; }
        counter3++;
    }
    if (status) {
        printf("Email address is okay.\n");
    }
    else {
        printf("Email address is outdated.\n");
    }
    
}