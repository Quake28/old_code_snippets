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
    x_length = budget
    y_length = len(players)
    dynamic_array = [[0 for aa in range(x_length + 1)] for ab in range(y_length + 2)]
    players_picked = [[False for aa in range(x_length + 1)] for ab in range(y_length + 2)]
    for y_pos in range(y_length - 1, -1, -1):
        cost = players[y_pos][1]
        form = players[y_pos][2]
        for x_pos in range(0, x_length + 1):
            if x_pos >= cost and (form + dynamic_array[y_pos + 1][x_pos - cost]) > dynamic_array[y_pos + 1][x_pos]:
                players_picked[y_pos][x_pos] = True
                dynamic_array[y_pos][x_pos] = form + dynamic_array[y_pos + 1][x_pos - cost]
            else:
                dynamic_array[y_pos][x_pos] = dynamic_array[y_pos + 1][x_pos]
    player_list = []
    form_cumulative = dynamic_array[0][x_length]
    for i in range(y_length + 1):
        if players_picked[i][x_length]:
            player_list.append(i)
            x_length -= players[i][1]
    return player_list, form_cumulative


budget = int(input())
player_count = int(input())
players = []
for a in range(player_count):
    input_string = input().split(",")
    input_string[1]=int(input_string[1])
    input_string[2]=float(input_string[2])
    players.append(input_string)
player_list, form_cumulative = knapsack(budget, players)
print("Bought Players:")
for player in range(len(player_list)):
    if player==0:
        print(players[player_list[player]][0],end=" ")
    else:
        print("->",players[player_list[player]][0],end=" ")
print()
print("Maximum summation of form: " + str(int(form_cumulative)))
