seconds=0
minutes=0
hours=0
days=0
weeks=0
months=0
years=0
yr1=0
yr2=0
mnth1=0
mnth2=0
date1=0
date2=0
print("This is a small program to calculate your approximate age.")
yr1=int(input("Enter your birth year :"))
mnth1=int(input("Enter the month number you were born in (eg.if February then enter 2) :"))
date1=int(input("Enter your birth date :"))
yr2=int(input("Enter current year :"))
mnth2=int(input("Enter current month (eg.if February then enter 2) :"))
date2=int(input("Enter today's date :"))
years=yr2-yr1-1
if(mnth1<mnth2):
    years=years+1
months=(years*12)+(12-mnth1)+mnth2
weeks=months*4
days=months*30+(30-date1)+date2
hours=days*24
minutes=hours*60
seconds=minutes*60
print("You are",years," years old")
print("You are",months," months old")
print("You are",weeks," weeks old")
print("You are",days," days old")
print("You are",hours," hours old")
print("You are",minutes," minutes old")
print("You are",seconds," seconds old")
