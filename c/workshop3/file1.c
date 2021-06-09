#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>


#define STRINGLENGTH 20
typedef char custom_string_1[STRINGLENGTH +1];

typedef struct{
	int Robot_Number; //of int type
	custom_string_1 Robot_Name; //string, up to 20 chars
	int Year_Manufacturer; //of int type, >=1990
	float Top_Speed; //of float type, >=0.0
	float Mass; //of float type, >0.0
} Robot;

void spaces(char* word){
	int i;
    for (i = 0; word[i] != '\0'; ++i){};
	for(int j=1; j<(STRINGLENGTH-i+1);j++){
		printf(" ");
	}
}
int main(){
	Robot Robot_info[100];
	int i=0;
	for(i=0;i<5;i++){
		//FAIRLY RANDOM INPUTS HERE, LOL
		Robot r1 = {1+i,"01234567890123456789",1234+i,12.3+i,123.4+i};
		Robot_info[i] = r1;
	}
	float finish_line_distance=0;
	int finish_time=0;
	char cont[4]="Yes";
	while((strcmp(cont,"Yes")==0)||(strcmp(cont,"yes")==0)||(strcmp(cont,"Y")==0)||(strcmp(cont,"y")==0)){
		while(finish_line_distance<=0){
			printf("Enter trial distance(in meters): ");
			scanf("%f",&finish_line_distance);
			if(finish_line_distance<=0){
				printf("Invalid value, please re-enter\n");
			}
		}
		while(finish_time<=0){
			printf("Enter trial time(in seconds): ");
			scanf("%i", &finish_time);
			if(finish_time<=0){
				printf("Invalid value, please re-enter\n");
			}
		}
		float Trial_speed = finish_line_distance/finish_time;
		printf("Robots capable of being used for a robotics competition with Trial_speed of %f (m/s):\n---------------------------------------------------------------------------------------------------------------------------------\n",Trial_speed);
		int count=0;
		for(int j=0;j<i;j++){
			if(i==0){
				printf("No robots is capable of being used for the robotics competition scenario!");
				break;
			}
			if (Robot_info[j].Top_Speed>=Trial_speed){
				printf("%i %s",Robot_info[j].Robot_Number,Robot_info[j].Robot_Name);
				spaces(Robot_info[j].Robot_Name);
				printf(" %i %.1f %.1f\n",Robot_info[j].Year_Manufacturer,Robot_info[j].Top_Speed,Robot_info[j].Mass);
				count+=1;
			}
		}
		printf("----------------------------------------------------------------------------------------------------------------------------------\nA total of %i robots are capable of being used for the robotics competition scenario\nDo you want to repeat the simulation?(Yes/No): ",count);
		char cont2[4];
		scanf("%4s",cont2);
		strcpy(cont,cont2);
		finish_line_distance=0;
		finish_time=0;
	}
}
