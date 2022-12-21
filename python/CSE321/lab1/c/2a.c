#include <stdio.h>

void add(int num1, int num2) {
    printf("Result is : %d\n",num1+num2);
}

void subtract(int num1, int num2) {
    printf("Result is : %d\n",num1-num2);
}

void multiply(int num1, int num2) {
    printf("Result is : %d\n",num1*num2);
}


void main() {
    int num1, num2, calcNum;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);
    while (1) {
        printf("Enter +/-/* for operation: ");
        char symbol;
        scanf(" %c",&symbol);
        if ((symbol=='+')||(symbol=='-')||(symbol=='*')) {
            break;
        }
        printf("Wrong input,\n");
    }
    if (num1<num2) {add(num1,num2);}
    else if (num1>num2) {subtract(num1,num2);}
    else {multiply(num1,num2);}
}