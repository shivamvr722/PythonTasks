players = {"red":{"R1": 0, "R2": 0, "R3": 0, "R4": 0}, "blue":{"B1": 0, "B2": 0, "B3": 0, "B4": 0}, "green":{"G1": 0, "G2": 0, "G3": 0, "G4": 0}, "yellow":{"Y1": 0, "Y2": 0, "Y3": 0, "Y4": 0}}

home_coordinated = {"red":{"R1":(2, 2), "R2":(2, 3), "R3":(3, 2), "R4":(3, 3)}, "blue":{"B1":(2, 11), "B2":(2, 12), "B3":(3, 11), "B4":(3, 12)},"green": {"G1":(11, 2), "G2":(11, 3), "G3":(12, 2), "G4":(12, 3)}, "yellow":{"Y1":(11, 11), "Y2":(11, 12), "Y3":(12, 11), "Y4":(12, 12)}}


# path_coordinates = ((6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (0, 6), (2, 6), (3, 6), (4, 6), (5, 6), (9, 6), (10, 6), (11, 6), (13, 6), (14, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (0, 8), (1, 8), (3, 8), (4, 8), (5, 8), (9, 8), (10, 8), (11, 8), (12, 8), (14, 8), (6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11), (6, 12), (7, 12), (7, 13), (8, 13), (6, 14), (7, 14), (8, 14))

# all
path_cordinates = ((6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11), (6, 12), (7, 12), (8, 12), (6, 13), (7, 13), (8, 13), (6, 14), (7, 14), (8, 14))



def home(row, column):
    for player, kukis in players.items():
        for player_key in home_coordinated.keys():
            if player_key == player:
                for kuki in kukis.keys():
                    if players[player][kuki] == 0:
                        if home_coordinated[player][kuki][0] == column and home_coordinated[player][kuki][1] == row:
                            print("{:>6}".format(kuki), end="  ")
                    elif home_coordinated[player][kuki][0] == column and home_coordinated[player][kuki][1] == row:
                        print("{:>6}".format("[ ]"), end="  ")



########################## show board #########################
def show_board(player, kuki, dice):
    rowcolpath = (6,7,8)
    homepath = (2,3,11,12)

    players[player][kuki] = players[player][kuki] + dice
    print(f"{player}{kuki}: {players[player][kuki]}")

    print("\n")
    for row in range(15):
        for column in range(15):
            if row in homepath and column in homepath:
                home(row, column)
            else:
                if row in rowcolpath or column in rowcolpath:
                    if row in rowcolpath and column in rowcolpath:
                        print("{:>6}".format("[ H ]"), end="  ")
                    else:
                        if row == 6 and column == 12 or row == 8 and column == 13 or row == 8 and column == 2 or row == 6 and column == 1 or row == 2 and column == 6 or row == 1 and column == 8 or row == 13 and column == 6 or row == 12 and column == 8:
                            print("{:>6}".format("( S )"), end="  ")
                        else:
                            temp = row
                            downpoz = 13 - players[player][kuki]
                            if column == 6 and column == downpoz:
                                if row == downpoz and column == 6:  
                                    row = "B1"
                            print("{:>6}".format(f"({row}, {column})"), end="  ")

                else:
                    print("{:>6}".format(" # "), end="  ")

        print("\n\n")
############################ show board #########################

def start_game(players):
    current_player = 0
    dice = 3
    show_board("blue", "B1", dice)

def ask_players():
    no_of_players = 0
    while no_of_players < 2:
        try:
            no_of_players = int(input("Enter The Number of Player: ").strip(" "))
            print("\n")
            if no_of_players < 2:
                print("Atleast two players required")
                continue
            else:
                start_game(no_of_players)

        except Exception as e:
            print("Please Enter The Numeric Value Only")

def show_menu():
    show = True
    while show:
        print("\n 1. Start Game \n 2. Exit ")
        option = input("\nEnter The Option: ").strip(" ")
        if option == "1":
            ask_players()
        elif option == "2":
            return False
        else:
            print("\nEnter The Appropriate Option")


def main():
    start_game(2)

if __name__ == "__main__":
    main()

