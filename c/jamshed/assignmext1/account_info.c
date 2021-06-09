#include <stdio.h>
#include <string.h>

struct user{
    char name[50];
    int accnumber;
    double balance;
};

void low_balance_customer(struct user *pt);
void special_increament(struct user *pt);

int main(){
    int i;
    struct user customer[21];
    for(i=1;i<21;i++){
        printf("\ncustomer[%d] name:",i);
        gets(customer[i].name);
        printf("customer[%d] account number:",i);
        scanf("%d",&customer[i].accnumber);
        printf("customer[%d] balance:",i);
        scanf("%lf",&customer[i].balance);
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
    }
	low_balance_customer(customer);
    special_increament(customer);
    FILE *Bank_info = NULL;
    Bank_info = fopen("Bank_info.txt","w");
	char temp[1000]; 
    if(Bank_info!=NULL){
        for(i=1;i<21;i++){
			sprintf(temp, "customer[%d] name: %s\ncustomer[%d] balance: %f\n",i,customer[i].name,i,customer[i].balance);
            fprintf(Bank_info,temp);
        }
        fclose(Bank_info);
    }
    return 0;
}

void low_balance_customer(struct user *pt){
    int i;
    for(i=1;i<21;i++){
        if(pt[i].balance<200){
            printf("name: %s\n",pt[i].name);
		}
    }
}

void special_increament(struct user *pt){
    int i,sum;
    for(i=1;i<21;i++){
        if(pt[i].balance>1000){
            sum=pt[i].balance+100;
            printf("\nname: %s\n",pt[i].name);
            printf("accnum: %d\n",pt[i].accnumber);
            printf("new balance: %d\n",sum) ;
        }
    }
}

/*
Shihab1
1
100
Shihab2
2
100
Shihab3
3
100
Shihab4
4
100
Shihab5
5
100
Shihab6
6
100
Shihab7
7
100
Shihab8
8
100
Shihab9
9
100
Shihab
10
100
Shihab
11
100
Shihab
12
100
Shihab
13
100
Shihab
14
100
Shihab
15
100
Shihab
16
100
Shihab
17
100
Shihab
18
100
Shihab19
19
500
Shihab20
20
1001
*/
