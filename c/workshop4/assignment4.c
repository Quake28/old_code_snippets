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
    int Year_Manufactured;      // of int type, >=1990
    float Top_Speed;            // of float type, >=0.0
    float Mass;                 // of float type, >0.0
    float Best_Score;           //of float type, >0.0
} Robot;

typedef struct
{
    int Test_Num;
    int Robot_Number;
    float Finish_Line_Distance;
    float Finish_Line_Time;
    int Strength;
    float Test_Score;
} Simulation;

void newRobot(Robot *rb, int i, char *a, int b, float c, float d, float e);
int load_file(Robot *Robot_info);
char *filler(char *fill, int length, char *fill_mat, char *word);
void print_simulation_result(Robot rb, Simulation sm);
void robot_test(Robot *rb, Simulation *sm, int *return_temp);
int input_robot_num(Robot *rb, int count_rb);
void simulation_results(Robot *rb, Simulation *sm, int *temp);
void display_winners(Robot *rb, Simulation *sm, int *temp);
void search(Robot *rb, int *temp);
void input_information(Robot *rb, int *temp);
void save_robot_info(Robot *rb, int count_rb);
void save_all_results(Simulation *sm, int count_sm);

int main()
{
    Robot Robot_info[100];
    Simulation Simulation_Data[100];
    int count_rb = 0;
    int count_sm = 0;
    //initialization(Robot_info, Simulation_Data);
    count_rb = load_file(Robot_info);
    //Robot rb = {1, "MyRobot0123456789012", 10, 1.0, 12.0, 123.0};
    //Simulation sm = {1, 92, 1.0, 12.0, 12.34, 123.23};
    //print_simulation_result(Robot_info[0], sm);
    int menuInput = 1;
    int *temp = malloc(sizeof(int) * 2);
    temp[0] = count_rb;
    temp[1] = count_sm;
    while (1 == 1)
    {
        printf("\n1. Simulate a robot against a human opponent\n2. Display simulation results\n3. Display winners\n4. Search a robot by robot number or by robot name\n5. Input/update robot information\n6. Save all results\n7. Save robot information\n8. Exit\n");
        printf("\nChoose Menu item : ");
        scanf("%d", &menuInput);
        if (menuInput == 1)
        {
            robot_test(Robot_info, Simulation_Data, temp);
            count_sm = temp[1];
        }
        else if (menuInput == 2)
        {
            simulation_results(Robot_info, Simulation_Data, temp);
        }
        else if (menuInput == 3)
        {
            display_winners(Robot_info, Simulation_Data, temp);
        }
        else if (menuInput == 4)
        {
            search(Robot_info, temp);
        }
        else if (menuInput == 5)
        {
            input_information(Robot_info, temp);
        }
        else if (menuInput == 6)
        {
            save_all_results(Simulation_Data, temp[1]);
        }
        else if (menuInput == 7)
        {
            save_robot_info(Robot_info, temp[0]);
        }
        else if (menuInput == 8)
        {
            printf("Exiting program...\n");
            return 0;
        }
        else
        {
            printf("\nInvalid Input,\nPlease choose a valid menu item.\n");
        }
    }
    //count = load_file(Robot_info, count);
}

int input_robot_num(Robot *rb, int count_rb)
{
    int roboNum = -1;
    while ((roboNum > count_rb) || (roboNum <= 0))
    {
        printf("Enter Robot number: ");
        scanf("%d", &roboNum);
        if (roboNum > count_rb)
        {
            printf("Robot number is not avaiable, please try again.\n");
        }
        else if (roboNum <= 0)
        {
            printf("Invalid Input\nRobot number cannot be zero or negative, pleast try again.\n");
        }
    }
    return roboNum - 1;
}

void newRobot(Robot *rb, int i, char *a, int b, float c, float d, float e)
{
    Robot r1 = {i + 1, "", b, c, d, e};
    strcpy(r1.Robot_Name, a);
    rb[i] = r1;
}

int load_file(Robot *Robot_info)
{
    FILE *fileR = fopen("Robot.txt", "r");
    int i = 0;
    //for (i = 0; i < 10; i++)
    while (1 == 1)
    {

        i++;
        int x = 0;
        char a[20];
        int b;
        float c;
        float d;
        float e = 0.0;
        fscanf(fileR, "%d %s %d %f %f %f\n", &x, a, &b, &c, &d, &e);
        newRobot(Robot_info, x - 1, a, b, c, d, e);
        if ((feof(fileR)) || (i == 10)) //remove ==10 to remove limit
            break;
        //printf("%d %s %d %.2f %.2f\n", x, a, b, c, d);
    }
    fclose(fileR);
    return i;
}

char *filler(char *fill, int length, char *fill_mat, char *word)
{
    strcpy(fill, "");
    char *fill2 = malloc(sizeof(char) * 50);
    int i;
    for (i = 0; word[i] != '\0'; ++i)
    {
    };
    for (int j = 0; j <= (length - i); j++)
    {
        sprintf(fill2, "%s%s", fill, fill_mat);
        strcpy(fill, fill2);
    }
    return fill;
}

void print_simulation_result(Robot rb, Simulation sm)
{
    char *temp = malloc(sizeof(char) * 50);
    char *temp2 = malloc(sizeof(char) * 50);

    int column1 = 25;
    int column2 = 20;
    int column1_tabbed = column1 - 4;
    int total_length = column1 + column2 + 4; //47
    printf("\n+%s+\n", filler(temp2, total_length, "-", ""));
    printf("| Robot Test Result%s|\n", filler(temp2, total_length - 1, " ", "Robot Test Result"));
    printf("+%s+\n", filler(temp2, total_length, "-", ""));

    sprintf(temp, "%d", sm.Test_Num);
    printf("| Test ID:%s| %d", filler(temp2, column1, " ", "Test ID:"), sm.Test_Num);
    printf("%s|\n", filler(temp2, column2, " ", temp));

    printf("+%s+", filler(temp2, column1 + 1, "-", ""));
    printf("%s+\n", filler(temp2, column2 + 1, "-", ""));

    printf("| Robot information:%s| ", filler(temp2, column1, " ", "Robot information:"));
    printf("%s|\n", filler(temp2, column2, " ", ""));

    printf("+%s+", filler(temp2, column1 + 1, "-", ""));
    printf("%s+\n", filler(temp2, column2 + 1, "-", ""));

    sprintf(temp, "%d", rb.Robot_Number);
    printf("|     Robot number:%s| %d", filler(temp2, column1_tabbed, " ", "Robot number:"), rb.Robot_Number);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    printf("|     Robot name:%s| %s", filler(temp2, column1_tabbed, " ", "Robot name:"), rb.Robot_Name);
    printf("%s|\n", filler(temp2, column2, " ", rb.Robot_Name));
    sprintf(temp, "%d", rb.Year_Manufactured);
    printf("|     Year Manufactured:%s| %d", filler(temp2, column1_tabbed, " ", "Year Manufactured:"), rb.Year_Manufactured);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Top_Speed);
    printf("|     Top Speed:%s| %.2f", filler(temp2, column1_tabbed, " ", "Top Speed:"), rb.Top_Speed);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Mass);
    printf("|     Mass:%s| %.2f", filler(temp2, column1_tabbed, " ", "Mass:"), rb.Mass);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Best_Score);
    printf("|     Best Score:%s| %.2f", filler(temp2, column1_tabbed, " ", "Best Score:"), rb.Best_Score);
    printf("%s|\n", filler(temp2, column2, " ", temp));

    printf("+%s+\n", filler(temp2, total_length, "-", ""));
    printf("| Test Conditions:%s|\n", filler(temp2, total_length - 1, " ", "Test Conditions:"));
    printf("+%s+\n", filler(temp2, total_length, "-", ""));

    sprintf(temp, "%.2f", sm.Finish_Line_Distance);
    printf("|     Finish Line Distance:%s| %.2f", filler(temp2, column1_tabbed, " ", "Finish Line Distance:"), sm.Finish_Line_Distance);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", sm.Finish_Line_Time);
    printf("|     Finish Line Time:%s| %.2f", filler(temp2, column1_tabbed, " ", "Finish Line Time:"), sm.Finish_Line_Time);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%d", sm.Strength);
    printf("|     Strength:%s| %d", filler(temp2, column1_tabbed, " ", "Strength:"), sm.Strength);
    printf("%s|\n", filler(temp2, column2, " ", temp));

    printf("+%s+\n", filler(temp2, total_length, "-", ""));
    printf("| Simulation Results:%s|\n", filler(temp2, total_length - 1, " ", "Simulation Results:"));
    printf("+%s+\n", filler(temp2, total_length, "-", ""));

    sprintf(temp, "%.2f", sm.Test_Score);
    printf("|     Combat Effectiveness:%s| %.2f", filler(temp2, column1_tabbed, " ", "Combat Effectiveness:"), sm.Test_Score);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    printf("+%s+\n", filler(temp2, total_length, "-", ""));
}

void print_robot_info(Robot rb)
{
    char *temp = malloc(sizeof(char) * 50);
    char *temp2 = malloc(sizeof(char) * 50);

    int column1 = 25;
    int column2 = 20;
    int column1_tabbed = column1 - 4;
    int total_length = column1 + column2 + 4; //47
    printf("\n+%s+\n", filler(temp2, total_length, "-", ""));
    printf("| Robot information:%s|\n", filler(temp2, total_length, " ", " Robot information:"));

    printf("+%s+", filler(temp2, column1 + 1, "-", ""));
    printf("%s+\n", filler(temp2, column2 + 1, "-", ""));

    sprintf(temp, "%d", rb.Robot_Number);
    printf("|     Robot number:%s| %d", filler(temp2, column1_tabbed, " ", "Robot number:"), rb.Robot_Number);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    printf("|     Robot name:%s| %s", filler(temp2, column1_tabbed, " ", "Robot name:"), rb.Robot_Name);
    printf("%s|\n", filler(temp2, column2, " ", rb.Robot_Name));
    sprintf(temp, "%d", rb.Year_Manufactured);
    printf("|     Year Manufactured:%s| %d", filler(temp2, column1_tabbed, " ", "Year Manufactured:"), rb.Year_Manufactured);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Top_Speed);
    printf("|     Top Speed:%s| %.2f", filler(temp2, column1_tabbed, " ", "Top Speed:"), rb.Top_Speed);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Mass);
    printf("|     Mass:%s| %.2f", filler(temp2, column1_tabbed, " ", "Mass:"), rb.Mass);
    printf("%s|\n", filler(temp2, column2, " ", temp));
    sprintf(temp, "%.2f", rb.Best_Score);
    printf("|     Best Score:%s| %.2f", filler(temp2, column1_tabbed, " ", "Best Score:"), rb.Best_Score);
    printf("%s|\n", filler(temp2, column2, " ", temp));

    printf("+%s+", filler(temp2, column1 + 1, "-", ""));
    printf("%s+\n", filler(temp2, column2 + 1, "-", ""));
}

void robot_test(Robot *rb, Simulation *sm, int *return_temp)
{
    int count_rb = return_temp[0];
    int count_sm = return_temp[1];
    int robot_num = input_robot_num(rb, count_rb);
    float finish_line_distance = 0.0;
    float finish_line_time = 0;
    int strength = -1;
    while (finish_line_distance <= 0.0)
    {
        printf("Enter trial distance (in meters): ");
        scanf("%f", &finish_line_distance);
        if (finish_line_distance <= 0)
        {
            printf("Invalid input, please re-enter\n");
        }
    }
    while (finish_line_time <= 0)
    {
        printf("Enter trial time (in seconds): ");
        scanf("%f", &finish_line_time);
        if (finish_line_time <= 0)
        {
            printf("Invalid input, please re-enter\n");
        }
    }
    while ((strength < 0) || (strength > 100))
    {
        printf("Enter number of items the robot can lift: ");
        scanf("%d", &strength);
        if (strength <= -1)
        {
            printf("Invalid input,\nItem count cannot be negative, please re-enter\n");
        }
        else if (strength > 100)
        {
            printf("Invalid input,\nItem count cannot be more than 100, please re-enter\n");
        }
    }
    float speed;
    float test_score = 0;
    speed = finish_line_distance / finish_line_time;
    test_score = speed;
    if (test_score > 60)
    {
        test_score = 60;
    }
    srand(time(NULL));
    test_score += strength * 0.4 + rand() % 11 - 5;
    if (test_score < 0)
    {
        test_score = 0;
    }
    else if (test_score > 100)
    {
        test_score = 100;
    }
    //printf("%.2f\n", test_score);
    Simulation temp = {count_sm + 1, robot_num, finish_line_distance, finish_line_time, strength, test_score};
    print_simulation_result(rb[robot_num], temp);
    if (temp.Test_Score > rb[robot_num].Best_Score)
    {
        printf("Congratulations!\nYour robot has a new best score.\nWould you like to save this value and replace the old Best Score? [Yes/No]: ");
        char save_Best_Score_Prompt[4];
        scanf("%s", save_Best_Score_Prompt);
        if ((strcmp(save_Best_Score_Prompt, "Yes") == 0) || (strcmp(save_Best_Score_Prompt, "yes") == 0) || (strcmp(save_Best_Score_Prompt, "Y") == 0) || (strcmp(save_Best_Score_Prompt, "y") == 0))
        {
            rb[robot_num].Best_Score = temp.Test_Score;
        }
    }
    printf("Would you like to save this simulation to the simulation database? [Yes/No]: ");
    char save_simulation_Prompt[4];
    scanf("%s", save_simulation_Prompt);
    if ((strcmp(save_simulation_Prompt, "Yes") == 0) || (strcmp(save_simulation_Prompt, "yes") == 0) || (strcmp(save_simulation_Prompt, "Y") == 0) || (strcmp(save_simulation_Prompt, "y") == 0))
    {
        sm[count_sm] = temp;
        //printf("%d %d %.2f %.2f %d %.2f", sm[count_sm].Test_Num, sm[count_sm].Robot_Number + 1, sm[count_sm].Finish_Line_Distance, sm[count_sm].Finish_Line_Time, sm[count_sm].Strength, sm[count_sm].Test_Score);
        //print_simulation_result(rb[robot_num], sm[count_sm]);
        count_sm++;
    }
    return_temp[0] = count_rb;
    return_temp[1] = count_sm;
}

void simulation_results(Robot *rb, Simulation *sm, int *temp)
{
    if (temp[1] == 0)
    {
        printf("No simulation data to preview.\nPlease run simulations first.\n");
        return;
    }
    int status = 0;
    char robotName[20];
    while (status == 0)
    {
        printf("Enter Robot name: ");
        scanf("%s", robotName);
        for (int i = 0; i < temp[1]; i++)
        {
            if ((strcmp(robotName, rb[sm[i].Robot_Number].Robot_Name) == 0) || (strcmp(robotName, "All") == 0) || (strcmp(robotName, "all") == 0) || (strcmp(robotName, "ALL") == 0))
            {
                print_simulation_result(rb[sm[i].Robot_Number], sm[i]);
                status++;
            }
        }
        if (status == 0)
        {
            printf("This robot name is unavailable or no simulation has been run for this robot yet.\n");
        }
    }
}

void display_winners(Robot *rb, Simulation *sm, int *temp)
{
    if (temp[1] == 0)
    {
        printf("No simulation data to preview.\nPlease run simulations first.\n");
        return;
    }
    int bestSpeed = 0;
    int bestStrength = 0;
    int bestCombatEffectiveness = 0;
    for (int i = 0; i < temp[1]; i++)
    {
        if (rb[sm[i].Robot_Number].Top_Speed > rb[sm[bestSpeed].Robot_Number].Top_Speed)
        {
            bestSpeed = i;
        }
        if (sm[i].Strength > sm[bestStrength].Strength)
        {
            bestStrength = i;
        }
        if (sm[i].Test_Score > sm[bestStrength].Test_Score)
        {
            bestCombatEffectiveness = i;
        }
    }
    printf("\nBest Speed:");
    print_simulation_result(rb[sm[bestSpeed].Robot_Number], sm[bestSpeed]);
    printf("\nBest Strength:");
    print_simulation_result(rb[sm[bestStrength].Robot_Number], sm[bestStrength]);
    printf("\nBest Combat Effectiveness:");
    print_simulation_result(rb[sm[bestCombatEffectiveness].Robot_Number], sm[bestCombatEffectiveness]);
}

void search(Robot *rb, int *temp)
{
    printf("\n1. Search by robot number\n2. Search by robot name\nEnter menu choice: ");
    int choice = 0;
    scanf("%d", &choice);
    if (choice == 1)
    {
        int roboNum = -2;
        while ((roboNum > temp[0]) || (roboNum < -1))
        {
            printf("Enter Robot number: ");
            scanf("%d", &roboNum);
            if (roboNum == -1)
            {
                for (int i = 0; i < temp[0]; i++)
                {
                    print_robot_info(rb[i]);
                }
            }
            else if (roboNum > temp[0])
            {
                printf("Robot number is not avaiable, please try again.\n");
                continue;
            }
            else if (roboNum <= -1)
            {
                printf("Invalid Input\nRobot number cannot be zero or negative (other than -1), pleast try again.\n");
            }
            else
            {
                print_robot_info(rb[roboNum - 1]);
            }
        }
    }
    else if (choice == 2)
    {
        int status = 0;
        char robotName[20];
        while (status == 0)
        {
            printf("\nEnter Robot name: ");
            scanf("%s", robotName);
            for (int i = 0; i < temp[0]; i++)
            {
                if ((strcmp(robotName, rb[i].Robot_Name) == 0) || (strcmp(robotName, "All") == 0) || (strcmp(robotName, "all") == 0) || (strcmp(robotName, "ALL") == 0))
                {
                    print_robot_info(rb[i]);
                    status++;
                }
            }
            if (status == 0)
            {
                printf("This robot name is unavailable.\nPlease input a valid robot name\n");
            }
        }
    }
}

void input_information(Robot *rb, int *temp)
{
    //int robotNum = input_robot_num(rb, temp[0]);
    //print_robot_info(rb[robotNum]);
    int roboNum = 0;
    printf("Enter Robot number: ");
    scanf("%d", &roboNum);
    custom_string_1 robot_Name;
    int year_Manufactured;
    float top_Speed;
    float mass;
    if ((roboNum >= temp[0]))
    {
        roboNum = temp[0];
        printf("Enter name: ");
        scanf("%s", robot_Name);
        printf("Enter the year of manufacturing: ");
        scanf("%d", &year_Manufactured);
        printf("Enter the top speed: ");
        scanf("%f", &top_Speed);
        printf("Enter the mass: ");
        scanf("%f", &mass);
        newRobot(rb, roboNum, robot_Name, year_Manufactured, top_Speed, mass, 0.0);
        temp[0]++;
    }
    else
    {
        printf("1. Name\n2. Year Manufactured\n3. Top Speed\n4. Mass\nChoose a value to change for robot number %d: ", roboNum);
        roboNum--;
        int choice;
        scanf("%d", &choice);
        if (choice == 1)
        {
            printf("Enter name: ");
            scanf("%s", robot_Name);
            strcpy(rb[roboNum].Robot_Name, robot_Name);
        }
        else if (choice == 2)
        {
            printf("Enter the year of manufacturing: ");
            scanf("%d", &year_Manufactured);
            rb[roboNum].Year_Manufactured = year_Manufactured;
        }
        else if (choice == 3)
        {
            printf("Enter the top speed: ");
            scanf("%f", &top_Speed);
            rb[roboNum].Top_Speed = top_Speed;
        }
        else if (choice == 4)
        {
            printf("Enter the mass: ");
            scanf("%f", &mass);
            rb[roboNum].Mass = mass;
        }
        else
        {
            printf("Invalid Input! Wrong menu item value.\n");
            return;
        }
    }
}

void save_all_results(Simulation *sm, int count_sm)
{
    if (count_sm == 0)
    {
        printf("No simulations completed yet.\nPlease complete simulations to save data.\n");
        return;
    }
    char *fileString = malloc(sizeof(char) * 100);
    FILE *fileW = fopen("Results.txt", "w");
    printf("Saving simulation data...\n");
    for (int i = 0; i < count_sm; i++)
    {
        sprintf(fileString, "%d %d %.2f %.2f %i %.2f\n", sm[i].Test_Num, sm[i].Robot_Number, sm[i].Finish_Line_Distance, sm[i].Finish_Line_Time, sm[i].Strength, sm[i].Test_Score);
        fprintf(fileW, fileString);
    }
    fclose(fileW);
    printf("Saving complete...\n");
}

void save_robot_info(Robot *rb, int count_rb)
{
    count_rb = 10; //Questions says restricted to 10 robots only, comment this line to remove limit
    char *fileString = malloc(sizeof(char) * 100);
    FILE *fileW = fopen("Robot.txt", "w");
    printf("Saving robot data...\n");
    for (int i = 0; i < count_rb; i++)
    {
        sprintf(fileString, "%d %s %d %.2f %.2f %.2f\n", rb[i].Robot_Number, rb[i].Robot_Name, rb[i].Year_Manufactured, rb[i].Top_Speed, rb[i].Mass, rb[i].Best_Score);
        fprintf(fileW, fileString);
    }
    fclose(fileW);
    printf("Saving complete...\n");
}