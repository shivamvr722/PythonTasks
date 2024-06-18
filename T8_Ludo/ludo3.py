import random

ludo_cordinated = []

for i in range(15):
    for j in range(15):
        ludo_cordinated.append((j, i))

path_cordinates = ((6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2), (6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11), (6, 12), (7, 12), (8, 12), (6, 13), (7, 13), (8, 13), (6, 14), (7, 14), (8, 14))

destination_cordinates = ((6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8))

safestart = ((8, 1), (6, 2), (1, 6), (2, 8), (6, 13), (8, 12), (12, 6), (13, 8))
redhome = ((2, 2), (3, 2), (2, 3), (3, 3))
bluehome = ((2, 11), (3, 11), (2, 12), (3, 12))
greenhome = ((11, 2), (12, 2), (11, 3), (12, 3))
yellowhome = ((11, 11), (12, 11), (11, 12), (12, 12))


path = (6,7,8)

def setcoinhome(position):
    i = 0
    for red in redhome:
        i += 1
        position = "R{i}"
    

path_cordinates = []

def board():
    counter = 0
    for position in ludo_cordinated:
        counter += 1
    
        for safe in safestart:
            if position[0] == safe[0] and position[1] == safe[1]:
                position = "[S]"
        
        # if position[0] in path and position[1] in path:
        #     position = "[x]"
        
        # for path in path_cordinates:
        #     if path[0] == position[0] or path[1] == position[1]:
        #         position = "| |"
        

        # for nospace in path_cordinates:
        #     if position[0] in nospace[0] or position[0] in nospace[1]:
        #         position = "#"
        #     else:
        #         position = "[]"
        
        if position[0] == counter and position[1] == counter:
            position = "#"

        r = 1
        for red in redhome:
            if position[0] == red[0] and position[1] == red[1]:
                position = f"R{r}"
            r += 1
        
        b = 1
        for blue in bluehome:
            if position[0] == blue[0] and position[1] == blue[1]:
                position = f"B{b}"
          
            b += 1
        
        g = 1
        for green in greenhome:
            if position[0] == green[0] and position[1] == green[1]:
                position = f"G{g}"
            g += 1

        y = 1
        for yellow in yellowhome:
            if position[0] == yellow[0] and position[1] == yellow[1]:
                position = f"Y{y}"
            y += 1
        
        
        # setcoinhome(position)
        



        print("{:>9}".format(f"{position}"), end="")    
        if counter == 15:
            print("\n\n")
            counter = 0

board()
print(path_cordinates)