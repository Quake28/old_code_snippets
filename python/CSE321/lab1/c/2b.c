#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main() {
    FILE *fileIn = fopen("input.txt","r");
    FILE *fileOut = fopen("output.txt","w");
    char *buffer1 = malloc(10000);
    char *character1 = malloc(8);
    char *character2 = malloc(8);
    character1[0] = getc(fileIn);
    while (character1[0] != EOF) {
        if (!((character2[0]==' ')&&(character1[0]==' '))) {
            buffer1 = strcat(buffer1,character1);
        }
        character2[0]=character1[0];
        character1[0] = getc(fileIn);
    }
    printf("%s\n",buffer1);
}