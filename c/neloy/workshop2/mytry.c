#include <stdio.h>
#include <stdlib.h>

int main(void)

{
	float finish_line_distance;
	float finish_line_time;
	float calculate_speed;
	int calculate_strength;
	
	printf("Please enter time (in seconds) : ");
	scanf("%f", &finish_line_time);
	
	printf("Please enter distance (in meters) : ");
	scanf("%f", &finish_line_distance);
	
	if (finish_line_time <=0 || finish_line_distance <=0)
	{
		printf("Error: Invalid data entered!\n");
	}
	else
	{
		calculate_speed = finish_line_distance/finish_line_time;
		printf("The robot has an average speed of %f meters per second.\n\n", calculate_speed);
	}
	
	
	printf("The strength of the robot is the number of objects it can successfully lift.\n");
	printf("Please enter a number between 0 and 100 : ");
	scanf("%i", &calculate_strength);
	
	if (calculate_strength <=0 || calculate_strength >100)
	{
		printf("Error: Please enter value between 0 and 100!\n");
	}
	else
	{
		calculate_strength = calculate_strength;
		printf("The robot has a strength of %i ", calculate_strength);
	}
	
	
	
return 0;
}
