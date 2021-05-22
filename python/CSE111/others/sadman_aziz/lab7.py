# Task-7


class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return "Name: " + self.__name + ", Team Name: " + self.__team


# write your code here
class Player(Football):
    def __init__(self, team_name, name, role, goal, played):
        super().__init__(team_name, name, role)
        self.goal = goal
        self.played = played

    def calculate_ratio(self):
        self.ratio = self.goal / self.played
        self.earning = (self.goal * 1000) + (self.played * 10)

    def print_details(self):
        print(super().get_name_team())
        print("Team Role:", self.role)
        print("Total Goal:", self.goal, " Total Played:", self.played)
        print("Goal Ratio:", self.ratio)
        print("Match Earning:", str(self.earning) + "k")


class Manager(Player):
    def __init__(self, team_name, name, role, goal, played=0):
        super().__init__(team_name, name, role, goal=0, played=0)
        self.earning=goal*1000
    def print_details(self):
        print(super().get_name_team())
        print("Team Role:", self.role)
        print("Total Win:", self.goal)
        print("Match Earning:", str(self.earning) + "k")

player_one = Player("Juventus", "Ronaldo", "Striker", 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print("------------------------------------------")
manager_one = Manager("Real Madrid", "Zidane", "Manager", 25)
manager_one.print_details()

"""
Name: Ronaldo, Team Name: Juventus
Team Role: Striker
Total Goal: 25, Total Played: 32
Goal Ratio: 0.78125
Match Earning: 25320K
----------------------------------
Name: Zidane, Team Name: Real Madrid
Team Role: Manager
Total Win: 25
Match Earning: 25000K
"""
