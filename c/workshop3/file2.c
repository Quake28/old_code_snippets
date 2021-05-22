#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define STRINGLENGTH 20
typedef char custom_string_1[STRINGLENGTH + 1];

typedef struct
{
    int Robot_Number;           // of int type
    custom_string_1 Robot_Name; // string, up to 20 chars
    int Year_Manufacturer;      // of int type, >=1990
    float Top_Speed;            // of float type, >=0.0
    float Mass;                 // of float type, >0.0
} Robot;

void spaces(char *word)
{
    int i;
    for (i = 0; word[i] != '\0'; ++i)
    {
    };
    for (int j = 1; j < (STRINGLENGTH - i + 1); j++)
    {
        printf(" ");
    }
}
void newRobot(Robot *rb, int i, char *a, int b, float c, float d)
{
    Robot r1 = {i + 1, "", b, c, d};
    strcpy(r1.Robot_Name, a);
    rb[i] = r1;
}
void individual_print(Robot *Robot_info, int j)
{
    printf("%i %s", Robot_info[j].Robot_Number, Robot_info[j].Robot_Name);
    spaces(Robot_info[j].Robot_Name);
    printf(" %i %.1f %.1f\n", Robot_info[j].Year_Manufacturer, Robot_info[j].Top_Speed, Robot_info[j].Mass);
}
void printer(Robot *rb, int index)
{
    printf("\nAll available robots:\n----------------------------------------------------------------------------\n");
    for (int x = 0; x < index; x++)
    {
        individual_print(rb, x);
    }
    printf("----------------------------------------------------------------------------\n");
}
int main()
{
    Robot Robot_info[100];
    int i = 0;
    char a[100];
    int b;
    float c;
    float d;

    // Preset inputs from pdf
    newRobot(Robot_info, i, "BeautyLink", 1999, 170, 110);
    i++;
    newRobot(Robot_info, i, "BigBrain", 2010, 92.5, 18);
    i++;
    newRobot(Robot_info, i, "LucyJar", 2013, 29.5, 17.5);
    i++;
    newRobot(Robot_info, i, "MiMi", 2018, 20.0, 10.8);
    i++;
    // Custom input
    newRobot(Robot_info, i, "Robot5", 2020, 30.0, 20.8);
    i++;

    float finish_line_distance = 0;
    int finish_time = 0;
    char cont[4] = "Yes";
    printer(Robot_info, i);
    while ((strcmp(cont, "Yes") == 0) || (strcmp(cont, "yes") == 0) || (strcmp(cont, "Y") == 0) ||
           (strcmp(cont, "y") == 0))
    {
        char input1[4] = "No";
        printf("\nDo you want to add robots(Yes/No) : ");
        scanf("%4s", input1);
        while ((strcmp(input1, "Yes") == 0) || (strcmp(input1, "yes") == 0) || (strcmp(input1, "Y") == 0) ||
               (strcmp(input1, "y") == 0))
        {
            if (i >= 100)
            {
                printf("\nSorry, the max limit of 100 robots has been reached\nYou may not add any more robots.\n");
                break;
            }
            printf("\nEnter Robot Name : ");
            scanf("%100s", a);
            printf("Enter manufacturing year : ");
            scanf("%i", &b);
            printf("Enter top speed : ");
            scanf("%f", &c);
            printf("Enter mass : ");
            scanf("%f", &d);
            newRobot(Robot_info, i, a, b, c, d);
            i++;
            printf("\nDo you want to continue adding more robots(Yes/No) : ");
            scanf("%4s", input1);
        }

        printer(Robot_info, i);
        printf("\n");
        while (finish_line_distance <= 0)
        {
            printf("Enter trial distance(in meters): ");
            scanf("%f", &finish_line_distance);
            if (finish_line_distance <= 0)
            {
                printf("Invalid value, please re-enter\n");
            }
        }

        while (finish_time <= 0)
        {
            printf("Enter trial time(in seconds): ");
            scanf("%i", &finish_time);
            if (finish_time <= 0)
            {
                printf("Invalid value, please re-enter\n");
            }
        }

        float Trial_speed = finish_line_distance / finish_time;
        printf("\nRobots capable of being used for a robotics competition with Trial_speed of %f (m/s):\n",
               Trial_speed);
        printf("----------------------------------------------------------------------------");
        int count = 0;

        printf("\n");
        for (int j = 0; j < i; j++)
        {
            if (i == 0)
            {
                printf("No robots is capable of being used for the robotics competition scenario!");
                break;
            }
            if (Robot_info[j].Top_Speed >= Trial_speed)
            {
                individual_print(Robot_info, j);
                count += 1;
            }
        }
        printf("----------------------------------------------------------------------------\n");
        printf("A total of %i robots are capable of being used for the robotics competition scenario\n", count);

        char input4[4] = "Yes";
        while ((strcmp(input4, "Yes") == 0) || (strcmp(input4, "yes") == 0) || (strcmp(input4, "Y") == 0) ||
               (strcmp(input4, "y") == 0))
        {
            printf("\n0: Skip searching\n1: Search with Robot Number\n2: Search with Robot Name\n");
            printf("3: Manufacturing year\n4: Top Speed\n5: Mass\n");
            printf("Enter search criteria : ");
            int input2;
            scanf("%d", &input2);
            printf("\n");
            int status = 0;
            if (input2 == 1)
            {
                int input3;
                printf("Please enter Robot Number to search : ");
                scanf("%d", &input3);
                printf("----------------------------------------------------------------------------\n");
                if (input3 >= i)
                {
                    printf("No robot available with Robot Number - %d\n", input3);
                }
                else
                {
                    individual_print(Robot_info, input3 - 1);
                }
                printf("----------------------------------------------------------------------------\n");
            }
            else if (input2 == 2)
            {
                char input3[100];
                printf("Please enter Robot Name to search : ");
                scanf("%100s", input3);
                printf("----------------------------------------------------------------------------\n");
                for (int z = 0; z < i; z++)
                {
                    if (strcmp(Robot_info[z].Robot_Name, input3) == 0)
                    {
                        individual_print(Robot_info, z);
                        status += 1;
                    }
                }
                if (status == 0)
                {
                    printf("No robots found with name - \"%s\"\n", input3);
                }
                printf("----------------------------------------------------------------------------\n");
            }
            else if (input2 == 3)
            {
                int input3;
                printf("Please enter manufacturing year to search : ");
                scanf("%d", &input3);
                printf("----------------------------------------------------------------------------\n");
                for (int z = 0; z < i; z++)
                {
                    if (Robot_info[z].Year_Manufacturer == input3)
                    {
                        individual_print(Robot_info, z);
                        status += 1;
                    }
                }
                if (status == 0)
                {
                    printf("No robots found with manufacturing year - %d\n", input3);
                }
                printf("----------------------------------------------------------------------------\n");
            }
            else if (input2 == 4)
            {
                float input3;
                printf("Please enter Top speed to search : ");
                scanf("%f", &input3);
                printf("----------------------------------------------------------------------------\n");
                for (int z = 0; z < i; z++)
                {
                    if (Robot_info[z].Top_Speed == input3)
                    {
                        individual_print(Robot_info, z);
                        status += 1;
                    }
                }
                if (status == 0)
                {
                    printf("No robots found with top speed - %f\n", input3);
                }
                printf("----------------------------------------------------------------------------\n");
            }
            else if (input2 == 5)
            {
                float input3;
                printf("Please enter mass to search : ");
                scanf("%f", &input3);
                printf("----------------------------------------------------------------------------\n");
                for (int z = 0; z < i; z++)
                {
                    if (Robot_info[z].Mass == input3)
                    {
                        individual_print(Robot_info, z);
                        status += 1;
                    }
                }
                if (status == 0)
                {
                    printf("No robots found with mass - %f\n", input3);
                }
                printf("----------------------------------------------------------------------------\n");
            }
            printf("Do you want to search more items?(Yes/No) : ");
            scanf("%4s", input4);
        }

        printf("Do you want to repeat the simulation?(Yes/No): ");
        char cont2[4];
        scanf("%4s", cont2);
        strcpy(cont, cont2);
        finish_line_distance = 0;
        finish_time = 0;

        printf("\n");
        printer(Robot_info, i);
    }
}
