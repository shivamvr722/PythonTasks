import random
# board

players = {}
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
    
    while len(random_list) <= len(snake_mouth):
        for sm in snake_mouth:
            n = random.randint(4,80)
            if n not in random_list and n not in snake_mouth:
                if sm > (n+15):
                    random_list.append(n)
                    snake_tail.append(n) 

    for m in snake_mouth:
        for r in random_list:
            if m > (r+15) and r not in snake_bites.values():
                snake_bites[m] = r

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
            if (n not in random_list2) and (n not in snake_mouth) and (n not in snake_tail) and (n not in ladder_start):
                if ls < n-15:
                    random_list2.append(n)
                    ladder_end.append(n)
    
    for s in ladder_start:
        for r in random_list2:
            if s < (r-15) and r not in ladders.values():
                ladders[s] = r

    # print(ladders)
    # print(snake_bites)

def show_board(no = 0, player="red"):
    print("\n\n")

    board_num = [range(1,11), range(20, 10, -1), range(21, 31), range(40, 30, -1), range(41, 51), range(60, 50, -1), range(61, 71), range(80, 70, -1), range(81, 91), range(100, 90, -1)]
    board_num = board_num[::-1]

    print("Dice: ", no)
    print(f"{player}: {players[player]} + {no} = {players[player] + no}")
    players[player] = players.get(player) + no
    print(players, "\n")

    # for player in players:
    for i in board_num:
        for j in i:
            if j in snake_bites.keys():
                j =  f"{str(j)}>~~{snake_bites[j]}"
                jsnake = j.split(">~~")[0]
                if int(jsnake) <= players[player]:
                    if int(jsnake) == players[player]:
                        players[player] = snake_bites[int(jsnake)]
                        j = f"{player}>~~{snake_bites[int(jsnake)]}"

            if j in ladders.keys():
                j =  f"{ladders[j]}|=|{str(j)}"
                jladder = j.split("|=|")[1]
                if int(jladder) <= players[player]:
                    if int(jladder) == players[player]:
                        players[player] = ladders[int(jladder)]
                        j = ladders[int(jladder)]
                        j = f"{ladders[int(jladder)]}|=|{player}"

            if j == players[player]:
                j = f"{str(j)} {player}"
            
            count = 0
            for px in players.keys():
                if j == players[px]:
                    j = f"{str(j)} {px}"

            print("{:>10}".format(j), end=" ")
        print("\n\n")

    # print("snakes ", snake_bites)
    # print("ladder ", ladders)







def start_game():
    dice_at_6_counter = 0
    player_list = [player for player in players.keys()]
    i = 0
    while players[player_list[i]] != 100:
        roll = input(f"{player_list[i]} Roll The Dice (N to Exit): ").strip(" ").lower()
        
        if roll == "n":
            return
        
        # n = roll_dice()
        # for manual input
        f = True
        while f:
            try:
                n = int(input("Enter The Dice value: ").strip(" "))
                f = False
            except Exception as e:
                print("Please Enter Numeric Value only")


        if (n + players[player_list[i]]) > 100:
            print("Dice: ", n)
            print(f"{player_list[i]} required points to win: {100 - players[player_list[i]]}")
            if i < len(player_list)-1:
                i += 1
            else:
                i = 0
            continue
        

        if n == 6:
            print("You Got 6, Roll Again!\n")
            dice_at_6_counter += 1
            show_board(n, player_list[i])
            if dice_at_6_counter == 3:
                # players[player_list[i]] = 0
                dice_at_6_counter = 0
                if i < len(player_list)-1:
                    i += 1
                else:
                    i = 0
            continue

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
                n_players -= 1
                players[color[n_players]] = 0

            if len(players) >= 2:
                random_snake_generator()
                random_ladder_generator()
                start_game()

        elif option == "2":
            main_menu = False
        else:
            print("Enter Valid option")



if __name__ == "__main__":
    main()
