path = (6,7,8)
home_rs = ((6, 2), (8, 1), (12, 6), (13, 8), (8, 12), (6, 13), (2, 8), (1, 6))


for column in range(15):
    for row in range(15):
        if row in path or column in path:
            if row in path and column in path:
                print("{:>3}".format("[X]"), end=" ")
            else:
                pass 
                # for rs in home_rs:
                # if row == home_rs[0][0] and column == home_rs[0][1]:
                #     print("{:>3}".format("[S]"), end=" ")

                # if row != home_rs[0][0] and column != home_rs[0][1]:
                #     print("{:<3}".format("1"), end=" ")
                
            
            
        else:
            print("{:>3}".format("0"), end=" ")
    print("\n")