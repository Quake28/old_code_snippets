#include <stdio.h>

void main() {
    int checker[5] = {0,0,0,0,0}; //upper,lower,number,symbol,invalid char used
    //printf("%d\n",checker[0]);
    char lamePassword[10000];
    scanf("%s",lamePassword);
    //printf("%s\n",lamePassword);
    int counter = 0;
    //printf("%c,%d\n",64,64);
    while(lamePassword[counter]!='\0') {
        // printf("%c %d %d\n",lamePassword[counter],lamePassword[counter],counter);
        if((lamePassword[counter]>='A')&&(lamePassword[counter]<='Z')) {
            checker[0]++;
        } 
        else if ((lamePassword[counter]>='a')&&(lamePassword[counter]<='z')) {
            checker[1]++;
        } 
        else if ((lamePassword[counter]>='0')&&(lamePassword[counter]<='9')) {
            checker[2]++;
        } 
        else if ((lamePassword[counter]=='@')||(lamePassword[counter]=='#')||(lamePassword[counter]=='$')||(lamePassword[counter]=='_')) {
            checker[3]++;
        } 
        else {
            checker[4]++;
        }
        counter++;
    }
    // printf("%d\n",counter);
    // printf("%d %d %d %d %d\n",checker[0],checker[1],checker[2],checker[3],checker[4]);
    int errorCount = 0;
    if (checker[0]==0) {
        errorCount++;
        printf("Uppercase character missing");
    } if (checker[1]==0) {
        if (errorCount!=0) {
            printf(", ");
        }
        errorCount++;
        printf("Lowercase character missing");
    } if (checker[2]==0) {
        if (errorCount!=0) {
            printf(", ");
        }
        errorCount++;
        printf("Digit missing");
    } if (checker[3]==0) {
        if (errorCount!=0) {
            printf(", ");
        }
        errorCount++;
        printf("Special character missing");
    } 
    printf("\n");
    if (checker[4]>0) {
        errorCount++;
        printf("Invalid character present, only uppercase, lowercase, digits and symbols [ _ , $ , # , @ ] are allowed.\n");
    } 
    if (errorCount==0) {
        printf("OK\n");
    }
}