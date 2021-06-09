#include <stdio.h>
#include <string.h>
FILE *Zoomanagementsystem;
struct animal_info // information that will stored in each species' category
{
    // variables declared.
    char cagenumber[50]; // cage number of animal
    int number;
    char name[50];   // animal name for example: Tiger, Bear etc.
    char genus[50];  // for example Panthera Tigris
    char origin[50]; // whether it is born in wild,under captive breeding or from which country.
};
struct workers
{
    // variables declared.
    char name[50];
    char entry[50];
    char leaving[50];
    char post[50];
    int ID;
};

void insertandupdateworkers(struct workers *pt, int wonum);
void SearchByWorker(struct workers *pt, int wonum);
void insertandupdateanimals(struct animal_info *st, int annum);
void SearchByAnimal(struct animal_info *st, int annum);
//void Deletebyname(struct animal_info *st, int annum);

int main()
{
    int annum, wonum;

    int i;
    struct animal_info animal[100];
    struct workers worker[1000];

    printf("The zoo management system\n");
    printf("...................................................................................\n");
    // taking input from user(how many animals).
    printf("total number of species being listed:\n");
    scanf("%d", &annum);
    // taking input from user.
    for (i = 1; i <= annum; i++)
    {
        printf("Animal[%d]\n", i); // animal type labeled as Animal 1 or Animal 4.
        printf("cage number:\n");
        scanf("%s", animal[i].cagenumber); //if veterinarian or any manager then cage number none.
        printf("existing number:\n");
        scanf("%d", &animal[i].number);
        printf("name:\n");
        fflush(stdin);
        gets(animal[i].name);
        printf("genus:\n");
        gets(animal[i].genus);
        printf("origin:\n");
        gets(animal[i].origin);
    }
    FILE *Zoomanagementsystem; // opening a FILE to store informations under the tittle Zoo manage system.
    Zoomanagementsystem = (fopen("Zoomanagementsystem.txt", "w"));
    if (Zoomanagementsystem != NULL)
    {
        for (i = 1; i <= annum; i++)
        {

            fprintf(Zoomanagementsystem, "cage number: %s\n", animal[i].cagenumber);
            fprintf(Zoomanagementsystem, "existing number:%d\n", animal[i].number);
            fprintf(Zoomanagementsystem, "name:%s\n", animal[i].name);
            fprintf(Zoomanagementsystem, "genus:%s\n", animal[i].genus);
            fprintf(Zoomanagementsystem, "origin:%s\n", animal[i].origin);
        }

        fclose(Zoomanagementsystem);
    }

    printf("  \n");
    printf("total number of workers:\n");
    scanf("%d", &wonum);
    // taking input from use for workers.
    for (i = 1; i <= wonum; i++)
    {
        printf("Worker[%d]\n", i);
        fflush(stdin); // animal type labeled as Animal 1 or Animal 4.
        printf("Name:\n");
        gets(worker[i].name);
        printf("Entry time:\n");
        gets(worker[i].entry); // when does the worker enter and leave the zoo
        printf("Leaving time:\n");
        gets(worker[i].leaving);
        printf("post:\n");
        gets(worker[i].post); // veterinarian or cleaner( what type of job)
        fflush(stdin);
        printf("ID number:\n");
        scanf("%d", &worker[i].ID);
        fflush(stdin);
    }

    FILE *Zooworkers; // opening a FILE to store informations under the tittle Zoo manage system.
    Zooworkers = (fopen("Zooworkers.txt", "w"));
    if (Zooworkers != NULL)
    {
        for (i = 1; i <= wonum; i++)
        {

            fprintf(Zooworkers, "Name: %s\n", worker[i].name);
            fprintf(Zooworkers, "Entry time: %s\n", worker[i].entry); // when does the worker enter and leave the zoo
            fprintf(Zooworkers, "Leaving time: %s\n", worker[i].leaving);
            fprintf(Zooworkers, "post: %s\n", worker[i].post); // veterinarian or cleaner( what type of job)
            fprintf(Zooworkers, "ID number: %d\n", worker[i].ID);
            fflush(stdin);
        }

        fclose(Zooworkers);
    }

    insertandupdateworkers(worker, wonum);
    insertandupdateanimals(animal, annum);
    SearchByAnimal(animal, annum);
    SearchByWorker(worker, wonum);
    //Deletebyname(animal, annum);

    return 0;
}

void insertandupdateworkers(struct workers *pt, int wonum)
{
    char choice[4] = {'y', 'e', 's', '\0'};
    int num2, i;
    char choice4[5];

    printf("\n\nDo you want to add more for workers?\n");
    gets(choice4);
    if (strcmp(choice4, choice) == 0)
    {
        printf("total number of workers:\n");
        scanf("%d", &num2);
        // taking input from user for workers.
        for (i = 1; i <= num2; i++)
        {
            printf("Worker[%d]\n", i + wonum); // animal type labeled as Animal 1 or Animal 4.
            fflush(stdin);
            printf("Name:\n");
            gets(pt[i].name);
            printf("Entry time:\n");
            gets(pt[i].entry); // when does the worker enter and leave the zoo
            printf("Leaving time:\n");
            gets(pt[i].leaving);
            printf("post:\n");
            gets(pt[i].post); // veterinarian or cleaner( what type of job)
            fflush(stdin);
            printf("ID number:\n");
            scanf("%d", &pt[i].ID);
        }

        FILE *Zooworkers; // opening a FILE to store informations under the tittle Zoo manage system.
        Zooworkers = (fopen("Zooworkers.txt", "a"));
        if (Zooworkers != NULL)
        {
            for (i = 1; i <= num2; i++)
            {
                fprintf(Zooworkers, "Worker[%d]\n", i + wonum); // animal type labeled as Animal 1 or Animal 4.
                fprintf(Zooworkers, "Name: %s\n", pt[i].name);
                fprintf(Zooworkers, "Entry time: %s\n", pt[i].entry); // when does the worker enter and leave the zoo
                fprintf(Zooworkers, "Leaving time: %s\n", pt[i].leaving);
                fprintf(Zooworkers, "post: %s\n", pt[i].post); // veterinarian or cleaner( what type of job)
                fprintf(Zooworkers, "ID number: %d\n", pt[i].ID);
            }

            fclose(Zooworkers);
        }
    }
    else
    {
        printf("Thanks!\n");
    }
}
void insertandupdateanimals(struct animal_info *st, int annum)
{
    char choice[4] = {'y', 'e', 's', '\0'};
    int num, i;
    char choice3[5];
    printf("\n\nDo you want to add more for animals?\n");
    scanf("%s", choice3);
    if (strcmp(choice3, choice) == 0)
    {
        printf("total number of species being listed:\n");
        scanf("%d", &num);
        // taking input from user.
        for (i = 1; i <= num; i++)
        {
            printf("Animal[%d]\n", i + annum); // animal type labeled as Animal 1 or Animal 4.
            printf("cage number:\n");
            scanf("%s", st[i].cagenumber);
            printf("existing number:\n");
            scanf("%d", &st[i].number);
            printf("name:\n");
            fflush(stdin);
            gets(st[i].name);
            printf("genus:\n");
            gets(st[i].genus);
        }

        FILE *Zoomanagementsystem; // opening a FILE to store informations under the tittle Zoo manage system.
        Zoomanagementsystem = (fopen("Zoomanagementsystem.txt", "a"));
        if (Zoomanagementsystem != NULL)
        {
            for (i = 1; i <= num; i++)
            {

                fprintf(Zoomanagementsystem, "cage number:%s\n", st[i].cagenumber);
                fprintf(Zoomanagementsystem, "existing number:%d\n", st[i].number);
                fprintf(Zoomanagementsystem, "name:%s\n", st[i].name);
                fprintf(Zoomanagementsystem, "genus:%s\n", st[i].genus);
                fprintf(Zoomanagementsystem, "origin:%s\n", st[i].origin);
            }

            fclose(Zoomanagementsystem);
        }
    }
    else
    {
        printf("Thanks!\n");
    }
}

void SearchByAnimal(struct animal_info *st, int annum)
{
    char search[5];
    int i;
    printf("\n\nif you have any query,enter the animal's name:\n");
    fflush(stdin);
    gets(search);
    FILE *Zoomanagementsystem;
    Zoomanagementsystem = (fopen("Zoomanagementsystem", "r"));
    if (Zoomanagementsystem != NULL)
    {
        for (i = 1; i <= annum; i++)
        {

            fgets(st[i].cagenumber, 50, Zoomanagementsystem);
            fscanf(Zoomanagementsystem, "%d", &st[i].number);
            fgets(st[i].name, 50, Zoomanagementsystem);
            fgets(st[i].genus, 50, Zoomanagementsystem);
            fgets(st[i].origin, 50, Zoomanagementsystem);
        }
        fclose(Zoomanagementsystem);
    }
    for (i = 1; i <= annum; i++)
    {
        if (strcmp(st[i].name, search) == 0)
        {
            printf("cage number: %s\n", st[i].cagenumber);
            printf("existing number: %d\n", st[i].number);
            printf("name: %s\n", st[i].name);
            printf("genus: %s\n", st[i].genus);
            printf("origin: %s\n", st[i].origin);
        }
    }
}
void SearchByWorker(struct workers *pt, int wonum)
{
    char search[5];
    int i;
    printf("\n\nif you have any query,enter the worker's name:\n");
    fflush(stdin);
    gets(search);
    FILE *Zooworkers;
    Zooworkers = (fopen("Zooworkers", "r"));
    if (Zooworkers != NULL)
    {
        for (i = 1; i <= wonum; i++)
        {

            fgets(pt[i].name, 50, Zoomanagementsystem);
            fgets(pt[i].entry, 50, Zoomanagementsystem);
            fgets(pt[i].leaving, 50, Zoomanagementsystem);
            fgets(pt[i].post, 50, Zooworkers);
            fscanf(Zooworkers, "%d", &pt[i].ID);
        }
        fclose(Zoomanagementsystem);
    }
    for (i = 1; i <= wonum; i++)
    {
        if (strcmp(pt[i].name, search) == 0)
        {
            printf("name: %s\n", pt[i].name);
            printf("Entry time: %s\n", pt[i].entry);
            printf("Leaving time: %s\n", pt[i].leaving);
            printf("post: %s\n", pt[i].post);
            printf("ID: %d\n", pt[i].ID);
        }
    }
}
/*
void Deletebyname(struct animal_info *st, int annum)
{
    char choice1[4] = {'y', 'e', 's', '\0'};
    int i, temp;
    char search[10], choice[5];
    printf("\n\nDo you want to delete anything:");
    fflush(stdin);
    gets(choice);
    if (strcmp(choice, choice1) == 0)
    {
        printf("\nEnter the animal name you want to delete:\n");
        gets(search);
        FILE *Zoomanagementsystem;
        Zoomanagementsystem = (fopen("Zoomanagementsystem", "r"));
        if (Zoomanagementsystem != NULL)
        {
            for (i = 1; i <= annum; i++)
            {

                fgets(st[i].cagenumber, 50, Zoomanagementsystem);
                fscanf(Zoomanagementsystem, "%d", &st[i].number);
                fgets(st[i].name, 50, Zoomanagementsystem);
                fgets(st[i].genus, 50, Zoomanagementsystem);
                fgets(st[i].origin, 50, Zoomanagementsystem);
            }
            fclose(Zoomanagementsystem);
        }

        for (i = 1; i <= annum; i++)
        {
            if (strcmp(st[i].name, search) != 0)
            {
                strcpy(st[i].name, '\0');
                strcpy(st[i].genus, '\0');
                strcpy(st[i].origin, '\0');
                temp = st[i].number;
                strcpy(st[i].cagenumber, '\0');

                FILE *Zoomanagementsystem; // opening a FILE to store informations under the tittle Zoo manage system.
                Zoomanagementsystem = (fopen("Zoomanagementsystem.txt", "w"));
                if (Zoomanagementsystem != NULL)
                {
                    for (i = 1; i <= annum; i++)
                    {

                        fprintf(Zoomanagementsystem, "cage number:%s\n", st[i].cagenumber);
                        fprintf(Zoomanagementsystem, "existing number:%d\n", st[i].number);
                        fprintf(Zoomanagementsystem, "name:%s\n", st[i].name);
                        fprintf(Zoomanagementsystem, "genus:%s\n", st[i].genus);
                        fprintf(Zoomanagementsystem, "origin:%s\n", st[i].origin);
                    }

                    fclose(Zoomanagementsystem);
                }
            }
        }
    }
    else
    {
        printf("Thanks!");
    }
}
*/