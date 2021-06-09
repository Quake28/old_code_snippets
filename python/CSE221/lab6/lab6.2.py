"""
15
6
Chelsea, 8, 9.6, Premier league
Inter Milan, 7, 9.4, Champion’s League
Individual, 5, 8.3, Coach of the Year
Real Madrid, 5, 8.7, Liga BBVA
Porto, 4, 8.5, Champion’s League
Mansister United, 6, 8.9, Europa League

Output:
Name of clubs whose trophies were sold:
Real Madrid -> Porto -> Mansister United
Maximum money he earned: 26.1 million
"""

def knapsack(budget, trophies):
    m = budget
    n = len(trophies)
    # initialization
    dp = [[0.00 for aa in range(m + 1)] for ab in range(n + 2)]
    path = [[False for aa in range(m + 1)] for ab in range(n + 2)]

    # finding optimum solution
    for idx in range(n - 1, -1, -1):
        weight = trophies[idx][1]
        price = trophies[idx][2]
        for budg in range(0, m + 1):
            if (
                budg >= weight
                and (price + dp[idx + 1][budg - weight]) > dp[idx + 1][budg]
            ):
                path[idx][budg] = True
                dp[idx][budg] = price + dp[idx + 1][budg - weight]
            else:
                dp[idx][budg] = dp[idx + 1][budg]

    # path printing
    taken = []  # will contain the trophies to take
    ans = dp[0][m]  # maximum price
    for i in range(n + 1):
        if path[i][m]:
            taken.append(i)
            m -= trophies[i][1]
    return taken, ans


if __name__ == "__main__":
    budget = int(input())
    count = int(input())
    trophies = []
    # trophies contains a 2d list where each element is list with a trophy's description
    for a in range(count):
        x = input().split(",")
        li = []
        li.append(x[0])
        li.append(int(x[1]))
        li.append(float(x[2]))
        li.append(x[3])
        trophies.append(li)
    bought, ans = knapsack(budget, trophies)
    final_list = ""
    print("Name of clubs whose trophies were sold:")
    for p in bought:
        final_list += trophies[p][0]
        final_list += " -> "
    print(final_list[:-4])
    print("Maximum money he earned: " + str(round(ans, 4)) + " million")
