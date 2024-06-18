import random
# board
# players = {"blue": 0, "green": 0, "red": 0, "yellow": 0}
players = {}
# snake_bites = {99: 2, 98: 6, 95: 47, 93: 31, 82: 25, 87: 46, 78: 40, 72: 30, 64: 22, 67: 54, 58: 24, 45: 20, 39: 21, 32: 9, 15: 5}
# ladders = {8: 27, 11: 33, 18: 42, 23: 57, 26: 44, 34: 53, 37: 75, 48: 68, 55: 94, 56: 81, 65: 97, 63: 85, 71: 91}

snake_bites = {}
ladders = {}

snake_mouth = []
snake_tail = []
ladder_start = []
ladder_end = []


random_list = []

def random_snake_generator():
    while len(snake_mouth) < 13:
        for _ in range(1, 13):
            n = random.randint(21,98)
            if n not in snake_mouth and n+1 not in snake_mouth and n-1 not in snake_mouth:
                snake_mouth.append(n)
                # print(snake_mouth)
    
    while len(random_list) <= len(snake_mouth):
        for sm in snake_mouth:
            n = random.randint(4,80)
            if n not in random_list:
                if sm > (n+15):
                    random_list.append(n)
                    snake_tail.append(n) 

    for m in snake_mouth:
        for r in random_list:
            if m > (r+15) and r not in snake_bites.values():
                snake_bites[m] = r
    # print(snake_bites)


random_list2 = []
def random_ladder_generator():
    while len(ladder_start) < 13:
        for _ in range(1, 13):
            n = random.randint(9,70)
            if (n not in ladder_start) and (n+1 not in ladder_start) and (n-1 not in ladder_start) and (n not in snake_mouth) and (n not in snake_tail):
                ladder_start.append(n)
    
    while len(random_list2) <= len(ladder_start):
        for ls in ladder_start:
            n = random.randint(30,95)
            if n not in random_list2 and n not in snake_mouth and n not in snake_tail:
                if ls < n-15:
                    random_list2.append(n)
                    ladder_end.append(n)
    
    for s in ladder_start:
        for r in random_list2:
            if s < (r-15) and r not in ladders.values():
                ladders[s] = r

    # print(ladders)



def show_board(no = 0, player="red"):

    players[player] = players.get(player) + no

    board_num = [range(1,11), range(20, 10, -1), range(21, 31), range(40, 30, -1), range(41, 51), range(60, 50, -1), range(61, 71), range(80, 70, -1), range(81, 91), range(100, 90, -1)]
    board_num = board_num[::-1]
    

    print("Dice: ", no)
    print(f"{player} : ", players[player])
    print(players)
    

    # for player in players:
    for i in board_num:
        for j in i:
            if j in snake_bites.keys():
                j =  f"{str(j)}>~~{snake_bites[j]}"
                jsnake = j.split(">~~")[0]
                # print((jsnake, players[player], player), end="")
                if int(jsnake) <= players[player]:
                    if int(jsnake) == players[player]:
                        players[player] = snake_bites[int(jsnake)]
                        j = f"{player}>~~{snake_bites[int(jsnake)]}"
            
            if j in ladders.keys():
                j =  f"{ladders[j]}|=|{str(j)}"
                jladder = j.split("|=|")[1]
                # print((jladder, players[player], player), end="")
                if int(jladder) <= players[player]:
                    if int(jladder) == players[player]:
                        players[player] = ladders[int(jladder)]
                        j = f"{ladders[int(jladder)]}|=|{player}"

                    
            if j == players[player]:
                j = f"{str(j)} {player}"

            for px in players.keys():
                if j == players[px]:
                    j = f"{str(j)} {px}"

            print("{:>10}".format(j), end=" ")
        print("\n\n")

    # print("snakes ", snake_bites)
    # print("ladder ", ladders)


dice_count = {}
dice_roll_count = 0

def start_game():
    global dice_count

    player_list = [player for player in players.keys()]
    i = 0
    while players[player_list[i]] < 100:
        global dice_roll_count
        roll = input("Roll The Dice (N to Exit): ").strip(" ").lower()
        
        if roll == "n":
            return
        
        n = roll_dice()

        # for manual input
        # f = True
        # while f:
        #     try:
        #         n = int(input("Enter The Dice value: ").strip(" "))
        #         f = False
        #     except Exception as e:
        #         print("Please Enter Numeric Value only")

        
        # logic for the dice turns 
        dice_roll_count += 1
        dice_roll_count_turns = 3 * len(player_list)
        if n == 6 and dice_roll_count <= dice_roll_count_turns:
            dice_count[player_list[i]] = dice_count[player_list[i]] + n
            if dice_count[player_list[i]] >= 18:
                dice_roll_count = 0
                players[player_list[i]] = 0
                dice_count[player_list[i]] = 0
            print(dice_count)
        
        show_board(n, player_list[i])
        
        if i < len(player_list)-1:
            i += 1
        else:
            i = 0
    print("win: ",player_list[i])
    print("\n Game Over \n")
        

def roll_dice():
    return random.choice(range(1,7))


def main():
    print("\nWelcome To Snake and Ladder\n")
    
    main_menu = True

    while main_menu:
        print("\n 1. Start Game \n 2. Exit")
        option = input("Enter Option: ").strip(" ")
        color = ("Red", "Gre", "Blu", "Yel")
        if option == "1":
            flag = True
            while flag:
                n_players = input("Enter The Numbers Of Players: ").strip(" ")
                try:
                    n_players = int(n_players)

                    if n_players < 2 or n_players > 5:
                        print("Less Then 2 Players and More the 4 Players are Not Allowed!")
                        continue
                    else:
                        flag = False
                except:
                    print("Enter Only Numeric Values!")
                    flag = True

            while n_players > 0:
                players[color[n_players]] = 0
                n_players -= 1

            if len(players) >= 2:
                random_snake_generator()
                random_ladder_generator()
                for p in players.keys():
                    dice_count[p] = 0
                start_game()

        elif option == "2":
            main_menu = False
        else:
            print("Enter Valid option")



if __name__ == "__main__":
    main()





# nflag = True
# player_name = input("Enter Name of Player (Min-Max 3 Char): ").strip(" ")

# while nflag:
#     if len(player_name) == 3:
#         nflag = False
#     else:
#         nflag = True
#         print("Enter 3 Char length name only!")

#     if player_name in players.keys():
#         pflag = True
#         print("same name not allowed!")
#     else:
#         pflag = False

#     if not pflag:
#         player_name = input("Enter Name of Player (Min-Max 3 Char): ").strip(" ")
