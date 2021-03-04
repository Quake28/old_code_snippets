lastWeekAvg=0
currWeekAvg=0
dayCount=0
weekCount=0
while True:
    while dayCount<7:
        caseCount=input("Daily cases? ")
        if caseCount=="":
            break
        elif int(caseCount)<0:
            print("Invalid input")
            continue
        else:
            currWeekAvg+=int(caseCount)
        dayCount+=1
    currWeekAvg=int(round(currWeekAvg/dayCount,0))
    print("{}-day average: {}".format(dayCount,currWeekAvg))
    if weekCount!=0:
        if currWeekAvg>lastWeekAvg:
            print("Average is more than last week")
        if currWeekAvg<lastWeekAvg:
            print("Average is lower than last week")
        else:
            print("Average is the same as last week")
    lastWeekAvg=currWeekAvg
    currWeekAvg=0
    weekCount+=1
    if dayCount!=7:
        break
    else:
        dayCount=0