#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

struct animal_info // information that will stored in each species' category
{
    // variables declared.
    char name[50];  // animal name for example: Tiger, Bear etc.
    char genus[50]; // for example Panthera Tigris
    int number;
    char origin[50];     // whether it is born in wild,under captive breeding or from which country.
    char cagenumber[50]; // cage number of animal
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

void insertandupdateworkers(struct workers *pt, int workerNum);
int SearchByWorker();
void insertandupdateanimals(struct animal_info *st, int animalNum);
int SearchByAnimal();
void writeWorker(struct workers *pt, int workerNum);
void writeAnimal(struct animal_info *st, int animalNum);
int readWorker(struct workers *pt);
int readAnimal(struct animal_info *st);
void deleteAnimal();
void deleteWorker();

int main()
{
    int animalNum, workerNum;
    int i;
    struct animal_info animal[100];
    struct workers worker[100];
    printf("The zoo management system\n");
    printf("...........................................\n"); // taking input from user(how many animals).
    printf("Total number of species being listed: ");
    scanf("%d", &animalNum); // taking input from user.
    for (i = 0; i < animalNum; i++)
    {
        printf("\nAnimal [%d]\n", i + 1); // animal type labeled as Animal 1 or Animal 4.
        printf("Cage number: ");
        scanf("%s", animal[i].cagenumber); //if veterinarian or any manager then cage number none.
        printf("Existing number: ");
        scanf("%d", &animal[i].number);
        printf("Name: ");
        scanf("%s", animal[i].name);
        printf("Genus: ");
        scanf("%s", animal[i].genus);
        printf("Origin: ");
        scanf("%s", animal[i].origin);
    }
    printf("\nTotal number of workers: ");
    scanf("%d", &workerNum);
    // taking input from use for workers.
    for (i = 0; i < workerNum; i++)
    {
        printf("Worker [%d]\n", i + 1); // animal type labeled as Animal 1 or Animal 4.
        printf("Name: ");
        scanf("%s", worker[i].name);
        printf("Entry time: ");
        scanf("%s", worker[i].entry); // when does the worker enter and leave the zoo
        printf("Leaving time: ");
        scanf("%s", worker[i].leaving);
        printf("Post: ");
        scanf("%s", worker[i].post); // veterinarian or cleaner( what type of job)
        printf("ID number:");
        scanf("%d", &worker[i].ID);
    }
    writeAnimal(animal, animalNum);
    writeWorker(worker, workerNum);
    insertandupdateanimals(animal, animalNum);
    insertandupdateworkers(worker, workerNum);
    int animalNotFound = SearchByAnimal();
    if (animalNotFound == -1)
    {
        printf("No animal was found with this name.\n");
    }
    int workerNotFound = SearchByWorker();
    if (workerNotFound == -1)
    {
        printf("No worker was found with this name.\n");
    }
    deleteAnimal();
    deleteWorker();
    return 0;
}

void writeWorker(struct workers *pt, int workerNum)
{
    FILE *Zooworkers = (fopen("Zooworkers.txt", "w")); // opening a FILE to store informations under the tittle Zoo manage system.
    if (Zooworkers != NULL)
    {
        for (int i = 0; i < workerNum; i++)
        {
            if (strcmp(pt[i].name, "") != 0)
            {
                fprintf(Zooworkers, "%s ", pt[i].name);
                fprintf(Zooworkers, "%s ", pt[i].entry);
                fprintf(Zooworkers, "%s ", pt[i].leaving);
                fprintf(Zooworkers, "%s ", pt[i].post);
                fprintf(Zooworkers, "%d\n", pt[i].ID);
            }
        }
        fclose(Zooworkers);
    }
}

void writeAnimal(struct animal_info *st, int animalNum)
{
    FILE *Zoomanagementsystem = (fopen("Zoomanagementsystem.txt", "w")); // opening a FILE to store informations under the tittle Zoo manage system.
    if (Zoomanagementsystem != NULL)
    {
        for (int i = 0; i < animalNum; i++)
        {
            if (strcmp(st[i].name, "") != 0)
            {
                fprintf(Zoomanagementsystem, "%s ", st[i].name);
                fprintf(Zoomanagementsystem, "%s ", st[i].genus);
                fprintf(Zoomanagementsystem, "%d ", st[i].number);
                fprintf(Zoomanagementsystem, "%s ", st[i].origin);
                fprintf(Zoomanagementsystem, "%s\n", st[i].cagenumber);
            }
        }
        fclose(Zoomanagementsystem);
    }
}

int readWorker(struct workers *pt)
{
    FILE *Zooworkers = (fopen("Zooworkers.txt", "r"));

    char a[50] = "";
    char b[50] = "";
    char c[50] = "";
    char d[50] = "";
    int e;
    int x = 0;

    while (1 == 1)
    {
        fscanf(Zooworkers, "%s %s %s %s %d", a, b, c, d, &e);
        if (feof(Zooworkers))
        {
            //printf("%d", x);
            break;
        }
        //printf("%s %s %s %s %d\n", a, b, c, d, e);
        struct workers worker = {"", "", "", "", e};
        strcpy(worker.name, a);
        strcpy(worker.entry, b);
        strcpy(worker.leaving, c);
        strcpy(worker.post, d);
        pt[x] = worker;
        x++;
    }
    fclose(Zooworkers);
    return x;
}

int readAnimal(struct animal_info *st)
{
    FILE *Zoomanagementsystem = (fopen("Zoomanagementsystem.txt", "r"));

    char a[50] = "";
    char b[50] = "";
    int c;
    char d[50] = "";
    char e[50] = "";
    int x = 0;
    while (1 == 1)
    {
        fscanf(Zoomanagementsystem, "%s %s %d %s %s", a, b, &c, d, e);
        if (feof(Zoomanagementsystem))
        {
            //printf("%d", x);
            break;
        }
        //printf("%s %s %d %s %s\n", a, b, c, d, e);
        struct animal_info animal = {"", "", c, "", ""};
        strcpy(animal.name, a);
        strcpy(animal.genus, b);
        strcpy(animal.origin, d);
        strcpy(animal.cagenumber, e);
        st[x] = animal;
        x++;
    }
    fclose(Zoomanagementsystem);
    return x;
}

int SearchByAnimal()
{
    char search[15];
    int i;
    struct animal_info animalList[100];
    int animalCount = readAnimal(animalList);
    printf("\nEnter the name of animal to search:");
    scanf("%s", search);
    for (i = 0; i < animalCount; i++)
    {
        for (int j = 0; j < strlen(search); j++)
        {
            search[j] = tolower(search[j]);
        }
        char *temp = malloc(sizeof(char) * 100);
        strcpy(temp, animalList[i].name);
        for (int k = 0; k < strlen(temp); k++)
        {
            //if (isdigit(temp[k]) != 0)
            //{
            temp[k] = tolower(temp[k]);
            //}
        }
        if (strcmp(temp, search) == 0)
        {
            printf("Cage number: %s\n", animalList[i].cagenumber);
            printf("Existing number: %d\n", animalList[i].number);
            printf("Name: %s\n", animalList[i].name);
            printf("Genus: %s\n", animalList[i].genus);
            printf("Origin: %s\n", animalList[i].origin);
            return i;
        }
    }
    return -1;
}

int SearchByWorker()
{
    char *search = malloc(sizeof(char) * 100);
    int i;
    struct workers workerList[100];
    int workerCount = readWorker(workerList);
    printf("\nEnter the name of worker to search:");
    fflush(stdin);
    scanf("%s", search);
    for (i = 0; i < workerCount; i++)
    {
        for (int j = 0; j < strlen(search); j++)
        {
            search[j] = tolower(search[j]);
        }
        char *temp = malloc(sizeof(char) * 100);
        strcpy(temp, workerList[i].name);
        for (int k = 0; k < strlen(temp); k++)
        {
            temp[k] = tolower(temp[k]);
        }
        if (strcmp(temp, search) == 0)
        {
            printf("Name: %s\n", workerList[i].name);
            printf("Entry time: %s\n", workerList[i].entry);
            printf("Leaving time: %s\n", workerList[i].leaving);
            printf("Post: %s\n", workerList[i].post);
            printf("ID: %d\n", workerList[i].ID);
            return i;
        }
    }
    return -1;
}

void insertandupdateworkers(struct workers *pt, int wonum)
{
    char choice[4] = {'y', 'e', 's', '\0'};
    int num2, i;
    char choice4[5];

    printf("\n\nDo you want to add more for workers?\n");
    scanf("%s", choice4);
    if (strcmp(choice4, choice) == 0)
    {
        printf("total number of workers:\n");
        scanf("%d", &num2);
        // taking input from user for workers.
        for (i = 0; i < num2; i++)
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
            for (i = 0; i < num2; i++)
            {
                fprintf(Zooworkers, "%s ", pt[i].name);
                fprintf(Zooworkers, "%s ", pt[i].entry); // when does the worker enter and leave the zoo
                fprintf(Zooworkers, "%s ", pt[i].leaving);
                fprintf(Zooworkers, "%s ", pt[i].post); // veterinarian or cleaner( what type of job)
                fprintf(Zooworkers, "%d\n", pt[i].ID);
            }
            fclose(Zooworkers);
        }
    }
    else
    {
        printf("Thanks!\n");
    }
    fflush(stdin);
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
        for (i = 0; i < num; i++)
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
            for (i = 0; i < num; i++)
            {
                fprintf(Zoomanagementsystem, "%s ", st[i].name);
                fprintf(Zoomanagementsystem, "%s ", st[i].genus);
                fprintf(Zoomanagementsystem, "%d ", st[i].number);
                fprintf(Zoomanagementsystem, "%s ", st[i].origin);
                fprintf(Zoomanagementsystem, "%s\n", st[i].cagenumber);
            }

            fclose(Zoomanagementsystem);
        }
    }
    else
    {
        printf("Thanks!\n");
    }
    fflush(stdin);
}

void deleteAnimal()
{
    printf("\nTo delete animal,");
    struct animal_info animalList[100];
    int animalCount = readAnimal(animalList);
    int searchIndex = SearchByAnimal();
    if (searchIndex == -1)
    {
        printf("No animal was found with this name.\n");
        return;
    }
    struct animal_info dummyAnimal = {"", "", 0, "", ""};
    animalList[searchIndex] = dummyAnimal;
    writeAnimal(animalList, animalCount);
}

void deleteWorker()
{
    printf("\nTo delete worker,");
    struct workers workerList[100];
    int workerCount = readWorker(workerList);
    int searchIndex = SearchByWorker();
    if (searchIndex == -1)
    {
        printf("No worker was found with this name.\n");
        return;
    }
    struct workers dummyWorker = {"", "", "", "", 0};
    workerList[searchIndex] = dummyWorker;
    writeWorker(workerList, workerCount);
}

/*
10
Cage1
10
Tiger
Something1
SomethingAgain1
Cage2
20
Cat
Something2
SomethingAgain2
Cage3
30
Lion
Something3
SomethingAgain3
Cage4
40
Dog
Something4
SomethingAgain4
Cage5
50
Hyenas
Something5
SomethingAgain5
Cage6
60
Fox
Something6
SomethingAgain6
Cage7
70
Zebra
Something7
SomethingAgain7
Cage8
80
Giraffe
Something8
SomethingAgain8
Cage9
90
Deer
Something9
SomethingAgain9
Cage10
100
Hippopotamus
Something10
SomethingAgain10
10
John
0600
1100
Officer1
527001
Carly1
0600
1100
Veterinarian1
527002
Shihab
0600
1100
Head
527003
Samia
0600
1100
Veterinarian2
527004
Abrar
0600
1100
Cleaner1
527005
Shifa
0600
1100
Officer2
527006
Shaiane
0600
1100
Cleaner2
527007
Moin
0600
1100
GeneralStaff1
527008
Neloy
0600
1100
GeneralStaff2
527009
Sadia
0600
1100
Manager
527010
no
no



*/