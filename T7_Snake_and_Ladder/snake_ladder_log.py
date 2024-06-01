## board basic
# t1_to_10 = range(1,11)
# t11_to_20 = range(20, 10, -1)
# t21_to_30 = range(21, 31)
# t31_to_40 = range(40, 30, -1)
# t41_to_50 = range(41, 51)
# t51_to_60 = range(60, 50, -1)
# t61_to_70 = range(61, 71)
# t71_to_80 = range(80, 70, -1)
# t81_to_90 = range(81, 91)
# t91_to_100 = range(100, 90, -1)


# board_num = [t1_to_10, t11_to_20, t21_to_30, t31_to_40, t41_to_50, t51_to_60, t61_to_70, t71_to_80, t81_to_90, t91_to_100]
# board_num = board_num[::-1]
# for i in board_num:
#     for j in i:
#         print("{:>5}".format(j), end=" ")
#     print("\n")



## board with snakes
# print("\nWelcome To Snake and Ladder\n")
# t1_to_10 = range(1,11)
# t11_to_20 = range(20, 10, -1)
# t21_to_30 = range(21, 31)
# t31_to_40 = range(40, 30, -1)
# t41_to_50 = range(41, 51)
# t51_to_60 = range(60, 50, -1)
# t61_to_70 = range(61, 71)
# t71_to_80 = range(80, 70, -1)
# t81_to_90 = range(81, 91)
# t91_to_100 = range(100, 90, -1)


# board_num = [t1_to_10, t11_to_20, t21_to_30, t31_to_40, t41_to_50, t51_to_60, t61_to_70, t71_to_80, t81_to_90, t91_to_100]
# board_num = board_num[::-1]

# snake_mouth = [99, 98, 95, 93, 82, 87, 78, 72, 64, 67, 58, 45, 39, 32, 15]
# snake_tail = [2, 6, 47, 32, 25, 45, 40, 30, 22, 54, 24, 20, 21, 9, 5]

# t = 0
# for i in board_num:
#     for j in i:
#         if j in snake_mouth:
#             j =  f"{str(j)}>~~{snake_tail[t]}"
#             t += 1
#             snake_tail.append(int(j.split(">~~")[1]))
        
#         print("{:>10}".format(j), end=" ")
#     print("\n\n")



# # snakes bite
# snake_bite = {99: 2, 98: 6, 95: 47, 93: 32, 82: 25, 87: 45, 78: 40, 72: 30, 64: 22, 67: 54, 58: 24, 45: 20, 39: 21, 32: 9, 15: 5}
# print("snake bites", snake_bite)
# # snake_bite = {}
# # for key, value in zip(snake_mouth, snake_tail):
# #     snake_bite[key] = value



## board with snakes and ladders
# board
# print("\nWelcome To Snake and Ladder\n")
# t1_to_10 = range(1,11)
# t11_to_20 = range(20, 10, -1)
# t21_to_30 = range(21, 31)
# t31_to_40 = range(40, 30, -1)
# t41_to_50 = range(41, 51)
# t51_to_60 = range(60, 50, -1)
# t61_to_70 = range(61, 71)
# t71_to_80 = range(80, 70, -1)
# t81_to_90 = range(81, 91)
# t91_to_100 = range(100, 90, -1)


# board_num = [t1_to_10, t11_to_20, t21_to_30, t31_to_40, t41_to_50, t51_to_60, t61_to_70, t71_to_80, t81_to_90, t91_to_100]
# board_num = board_num[::-1]

# snake_mouth = [99, 98, 95, 93, 82, 87, 78, 72, 64, 67, 58, 45, 39, 32, 15]
# snake_tail = [2, 6, 47, 31, 25, 46, 40, 30, 22, 54, 24, 20, 21, 9, 5]


# ladder_start = [8, 11, 18, 23, 26, 34, 37, 48, 55, 56, 65, 63, 71]
# ladder_end = [27, 33, 42, 57, 44, 53, 75, 67, 94, 98, 97, 99, 91][::-1]


# sc = 0
# sd = 0

# for i in board_num:
#     for j in i:
#         if j in snake_mouth:
#             j =  f"{str(j)}>~~{snake_tail[sc]}"
#             sc += 1
        
#         if j in ladder_start:
#             j =  f"{ladder_end[sd]}|=|{str(j)}"
#             sd += 1

#         print("{:>10}".format(j), end=" ")
#     print("\n\n")



# # snakes bite
# snake_bite = {99: 2, 98: 6, 95: 47, 93: 31, 82: 25, 87: 46, 78: 40, 72: 30, 64: 22, 67: 54, 58: 24, 45: 20, 39: 21, 32: 9, 15: 5}
# ladder =  {8: 27, 11: 33, 18: 42, 23: 44, 26: 57, 34: 53, 37: 75, 48: 67, 55: 94, 56: 98, 65: 97, 63: 99, 71:91}
# print("snakes ", snake_bite)
# print("ladder ", ladder)



$$$$$$$$ 41 45 $$$$$$$
        41 $$$$$$$$ 42 45 $$$$$$$
        42 $$$$$$$$ 43 45 $$$$$$$
        43 $$$$$$$$ 44 45 $$$$$$$
        44 yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
$$$$$$$$ blue>~~20 20 $$$$$$$
 blue>~~20 $$$$$$$$ 46 20 $$$$$$$
        46 $$$$$$$$ 47 20 $$$$$$$
        47 $$$$$$$$ 94|=|48 20 $$$$$$$
   94|=|48 $$$$$$$$ 49 20 $$$$$$$
        49 $$$$$$$$ 50 20 $$$$$$$
        50 


$$$$$$$$ 20 11 $$$$$$$
        20 $$$$$$$$ 19 11 $$$$$$$
        19 $$$$$$$$ 57|=|18 11 $$$$$$$
   57|=|18 $$$$$$$$ 17 11 $$$$$$$
        17 $$$$$$$$ 16 11 $$$$$$$
        16 $$$$$$$$ 15>~~9 11 $$$$$$$
    15>~~9 $$$$$$$$ 14 11 $$$$$$$
        14 $$$$$$$$ 13 11 $$$$$$$
        13 $$$$$$$$ 12 11 $$$$$$$
        12 XXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$$$$$$$$ 33|=|blue 33 $$$$$$$
 33|=|blue 