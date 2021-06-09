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
    x_length = budget
    y_length = len(trophies)
    dynamic_array = [[0.00 for aa in range(x_length + 1)] for ab in range(y_length + 2)]
    tophies_picked = [[False for aa in range(x_length + 1)] for ab in range(y_length + 2)]
    for y_pos in range(y_length - 1, -1, -1):
        weight = trophies[y_pos][1]
        price = trophies[y_pos][2]
        for x_pos in range(0, x_length + 1):
            if (
                x_pos >= weight
                and (price + dynamic_array[y_pos + 1][x_pos - weight]) > dynamic_array[y_pos + 1][x_pos]
            ):
                tophies_picked[y_pos][x_pos] = True
                dynamic_array[y_pos][x_pos] = price + dynamic_array[y_pos + 1][x_pos - weight]
            else:
                dynamic_array[y_pos][x_pos] = dynamic_array[y_pos + 1][x_pos]
    taken = []
    price_cumulative = dynamic_array[0][x_length]
    for i in range(y_length + 1):
        if tophies_picked[i][x_length]:
            taken.append(i)
            x_length -= trophies[i][1]
    return taken, price_cumulative


budget = int(input())
player_count = int(input())
trophies = []
for a in range(player_count):
    input_string = input().split(",")
    input_string[1]=int(input_string[1])
    input_string[2]=float(input_string[2])
    trophies.append(input_string)
trophy_list, price_cumulative = knapsack(budget, trophies)
print("Name of clubs whose trophies were sold:")
for trophy in range(len(trophy_list)):
    if trophy==0:
        print(trophies[trophy_list[trophy]][0],end=" ")
    else:
        print("->",trophies[trophy_list[trophy]][0],end=" ")
print()
print("Maximum money he earned: " + str(round(price_cumulative, 1)))
