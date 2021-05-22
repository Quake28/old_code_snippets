"""
150
6
Aubameyang, 80, 96, F
Koulibaly, 70, 94, D
Thiago, 45, 83, M
Insigne, 50, 87, F
Kimmich, 40, 85, D
Sancho, 60, 89, M

Output:
Bought Players:
Insigne -> Kimmich -> Sancho
Maximum summation of form: 261
"""


def knapsack(budget, players):
    m = budget
    n = len(players)
    # initialization
    dp = [[0 for aa in range(m + 1)] for ab in range(n + 2)]
    path = [[False for aa in range(m + 1)] for ab in range(n + 2)]
    # finding optimum solution
    for idx in range(n - 1, -1, -1):
        cost = players[idx][1]
        form = players[idx][2]
        for budg in range(0, m + 1):
            if budg >= cost and (form + dp[idx + 1][budg - cost]) > dp[idx + 1][budg]:
                path[idx][budg] = True
                dp[idx][budg] = form + dp[idx + 1][budg - cost]
            else:
                dp[idx][budg] = dp[idx + 1][budg]

    # path printing
    bought = []  # will contain the players to buy
    ans = dp[0][m]  # maximum form
    for i in range(n + 1):
        if path[i][m]:
            bought.append(i)
            m -= players[i][1]
    return bought, ans


if __name__ == "__main__":
    budget = int(input())
    count = int(input())
    players = []
    # players contains a 2d list where each element is list with a player's description
    for a in range(count):
        x = input().split(",")
        li = []
        for b in range(len(x)):
            try:
                li.append(int(x[b]))
            except:
                li.append(x[b])
        players.append(li)
    bought, ans = knapsack(budget, players)
    final_list = ""
    print("Bought Players:")
    for p in bought:
        final_list += players[p][0]
        final_list += " -> "
    print(final_list[:-4])
    print("Maximum summation of form: " + str(ans))
