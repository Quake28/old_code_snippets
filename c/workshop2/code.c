#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

float calculate_speed(float finish_line_distance, float finish_line_time){
	float speed;
	speed = finish_line_distance/finish_line_time;
	return speed;
}

int calculate_strength(){
	int weights_lifted;
	printf("Please enter number of weights lifted : ");
	scanf("%i", &weights_lifted);
	while(weights_lifted<0||weights_lifted>100){
		printf("\nInvalid input. Value not in range (0-100)!\nPlease re-enter number of weights lifted : ");
		scanf("%i", &weights_lifted);
	}
	return weights_lifted;
}

int calculate_combat(float speed, int strength){
	if(speed>60){
		speed=60.0;
	}
	int perf_score = speed + strength*2.0/5;
	srand(time(NULL));
	int robot = 0;
	int human = 0;
	int count = 0;
	int human_score;
	while(count<100){
		int robot_score = perf_score+rand()%11-5;
		if(robot_score<0){continue;}
		else if(robot_score>100){robot_score=100;}
		human_score=rand()%101;
		printf("%i %i ",robot_score,human_score);//comment out after debugging
		if(human_score>robot_score){
			human+=1;
			//printf("Human");//comment out after debugging
		}
		else if (human_score<robot_score){
			robot+=1;
			printf("Robot uprising");//comment out after debugging
		}
		printf("\n");//comment out after debugging
		count+=1;
	}
	return robot;
}

int main(void){
	float finish_line_distance;
	float finish_line_time;
	float speed,strength;
	int wins;
	char keep_running='y';
	while(keep_running=='Y'||keep_running=='y'){
		printf("Please enter time (in seconds) : ");
		scanf("%f", &finish_line_time);
		while(finish_line_time<0){
			printf("\nInvalid input! Value is negative.\nPlease re-enter time (in seconds) : ");
			scanf("%f", &finish_line_time);
		}
		printf("Please enter distance (in meters) : ");
		scanf("%f", &finish_line_distance);
		while(finish_line_distance<0){
			printf("\nInvalid input! Value is negative.\nPlease re-enter distance (in meters) : ");
			scanf("%f", &finish_line_distance);
		}
		speed = calculate_speed(finish_line_distance,finish_line_time);
		strength = calculate_strength();
		wins = calculate_combat(speed,strength);
		printf("The robot won %i simulations against a human.\n",wins);
		
		printf("Do you want to run the program again? (Y/N) : ");
		scanf(" %c", &keep_running);
	}
	return 0;
}
