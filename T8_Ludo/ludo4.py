import random 

ludo_cordinated = []
for i in range(15):
    for j in range(15):
        ludo_cordinated.append({(j, i) : ""})

players_position = {"red":{"R1": 6, "R2": 56, "R3": 56, "R4": 10}, "blue":{"B1": -1, "B2": -1, "B3": -1, "B4": -1}, "green":{"G1": -1, "G2": -1, "G3": -1, "G4": -1}, "yellow":{"Y1": -1, "Y2": -1, "Y3": -1, "Y4": -1}}

home_coordinated = {"red":{"R1":(2, 2), "R2":(2, 3), "R3":(3, 2), "R4":(3, 3)}, "blue":{"B1":(2, 11), "B2":(2, 12), "B3":(3, 11), "B4":(3, 12)},"green": {"G1":(11, 2), "G2":(11, 3), "G3":(12, 2), "G4":(12, 3)}, "yellow":{"Y1":(11, 11), "Y2":(11, 12), "Y3":(12, 11), "Y4":(12, 12)}}

destination_cordinates = ((7, 6), (6, 7), (8, 7), (7, 8))

# for home side borders 
home_side_borders = ((6, 6), (8, 6), (7, 7), (6, 8), (8, 8),)

# for borders 
border_cordinates = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (0, 2), (1, 2), (4, 2), (5, 2), (9, 2), (10, 2), (13, 2), (14, 2), (0, 3), (1, 3), (4, 3), (5, 3), (9, 3), (10, 3), (13, 3), (14, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (9, 4), (10, 4),(11, 4), (12, 4), (13, 4), (14, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (0, 11), (1, 11), (4, 11), (5, 11), (9, 11), (10, 11), (13, 11), (14, 11), (0, 12), (1, 12), (4, 12), (5, 12), (9, 12), (10, 12), (13, 12), (14, 12), (0, 13), (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (9, 13), (10, 13), (11, 13), (12, 13), (13, 13), (14, 13), (0, 14), (1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (9, 14), (10, 14), (11, 14), (12, 14), (13, 14), (14, 14))

# for all 
path_cordinates = ((6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (7, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11), (6, 12), (7, 12), (8, 12), (6, 13), (7, 13), (8, 13), (6, 14), (7, 14), (8, 14))

# blue path
blue_path_cordiantes = ((6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (7, 8))

# red path
red_path_cordinates = ((1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7))

# yellow path
yellow_path_cordinates = ((13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (13, 7), (12, 7), (11, 7), (10, 7), (9, 7), (8, 7))

# green path
green_path_cordinates = ((8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (6, 14), (6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6))

# safe zones 
safe_zone = ((8, 12), (6, 2), (12, 6), (2, 8))

# start cordinates 
start_cordinates = ((1, 6), (6, 13), (8, 1), (13, 8))

# red homes
redhome = ((2, 2), (3, 2), (2, 3), (3, 3))
bluehome = ((2, 11), (3, 11), (2, 12), (3, 12))
greenhome = ((11, 2), (12, 2), (11, 3), (12, 3))
yellowhome = ((11, 11), (12, 11), (11, 12), (12, 12))

# starting position
r_start = (6, 1)
b_start = (13, 6)
g_start = (1, 8)
y_start = (8, 13)




# home position
def set_home(ludo, player_color, home_cordinates):
    for player, coins in players_position.items():
        if player == player_color:
            for cordinate, color in zip(coins.items(), home_cordinates):
                if color == ludo and cordinate[1] == -1:
                    index = ludo_cordinated.index({ludo: ""})
                    ludo_cordinated[index][ludo] = "{:>7}".format(cordinate[0])
                    # ludo_cordinated[index][ludo] = cordinate[0]
                elif color == ludo:
                    index = ludo_cordinated.index({ludo: ""})
                    ludo_cordinated[index][ludo] = "{:>7}".format("[ ]")

def set_path_ways(ludo, cordinates, dictionary, set_with):
    for cords in cordinates:
        if ludo == cords:
            index = ludo_cordinated.index(dictionary)
            if set_with == "*":
                ludo_cordinated[index][ludo] = f"   {set_with}   "
            else:
                ludo_cordinated[index][ludo] = " {:>5} ".format(set_with)


def is_home(ludo):
    set_home(ludo, "red", redhome)
    set_home(ludo, "blue", bluehome)
    set_home(ludo, "green", greenhome)
    set_home(ludo, "yellow", yellowhome)

def pathways(ludo, dictionary):
    set_path_ways(ludo, home_side_borders, dictionary, "*")
    set_path_ways(ludo, border_cordinates, dictionary, "#")
    set_path_ways(ludo, path_cordinates, dictionary, "|  |")
    set_path_ways(ludo, destination_cordinates, dictionary, "| H |")
    set_path_ways(ludo, safe_zone, dictionary, "| s |")
    set_path_ways(ludo, start_cordinates, dictionary, "| S |")

def set_coin_operation(ludo, dictionary, coin_dict, cordinates):
    for coin, value in coin_dict.items():
        if value:

            cordinate = cordinates[value]
            if cordinate == ludo:
                index = ludo_cordinated.index(dictionary)
                ludo_cordinated[index][ludo] = " {:>5} ".format(f"| {coin} |")

# main control
def start_boarding(dice, c_player, c_coin):
    players_position[c_player][c_coin] = players_position[c_player][c_coin] + dice
    
    for ludo_dict in ludo_cordinated:
        for ludo in ludo_dict:
            # setting coins on home index
            is_home(ludo)
        # for setting up the path, safe zones and destination
        pathways(ludo, ludo_dict)
        
        # for setting up the player 
        for player, coin_dict in players_position.items():
            if player == "blue":
                set_coin_operation(ludo, ludo_dict, coin_dict, blue_path_cordiantes)
            if player == "red":
                set_coin_operation(ludo, ludo_dict, coin_dict, red_path_cordinates)
            if player == "yellow":
                set_coin_operation(ludo, ludo_dict, coin_dict, yellow_path_cordinates)
            if player == "green":
                set_coin_operation(ludo, ludo_dict, coin_dict, green_path_cordinates)



def start(n, c_player, c_coin):
    for player, coin_dict in players_position.items():
        if c_player == player:
            for coin in coin_dict:
                if coin == c_coin:
                    if players_position[c_player][coin] == -1 and n == 6:
                        players_position[c_player][c_coin] = 0
                        return True
                    else: 
                        return False



def game_menu():
    # n = random.randint(1,6)
    n = int(input("enter the no: "))
    if not start(n, "blue", "B1"):
        start_boarding(0, "blue", "B1") 
    else:
        start_boarding(n, "blue", "B1")

game_menu()


i = 0
for positions in ludo_cordinated:
    for key, position in positions.items():
        print(position, end=" ")
    # print(i, end="")
    i += 1
    if i == 15:
        print("\n\n")
        i = 0


print(players_position)