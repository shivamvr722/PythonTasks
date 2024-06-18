def empty_check(value):
    if value == "":
        print("\n! Empty Field Not Allowed !\n")
        return False
    else:
        return True

def check_isnumeric(value, msg):
    value_matrix = value
    while not value_matrix.isnumeric():
        print("\nPlease Enter Absolute Numeric Value")
        value_matrix = input(msg).strip(" ")
    return int(value_matrix)

go_on = True
while go_on:
    try:
        matrix1 = input("Enter The Name Of Matrix1: ").strip(" ")
        while not empty_check(matrix1):
            matrix1 = input("Enter The Name Of Matrix1: ").strip(" ")

        matrix2 = input("\nEnter The Name Of Matrix2: ").strip(" ")
        while not empty_check(matrix2):
            matrix2 = input("Enter The Name Of Matrix2: ").strip(" ")

        try:
            nrows = input(f"\nEnter  The  Number  Of Row For Matrix [{matrix1}]: ")
            nrows = check_isnumeric(nrows, f"\nEnter  The  Number  Of Row For Matrix [{matrix1}]: ")

            ncolumn = input(f"\nEnter The Number Of Column For Matrix [{matrix1}]: ")
            ncolumn = check_isnumeric(ncolumn, f"\nEnter The Number Of Column For Matrix [{matrix1}]: ")

            nrows2 = input(f"\nEnter  The  Number  Of Row For Matrix [{matrix2}]: ")
            nrows2 = check_isnumeric(nrows2, f"\nEnter  The  Number  Of Row For Matrix [{matrix2}]: ")

            ncolumn2 = input(f"\nEnter The Number Of Column For Matrix [{matrix2}]: ")
            ncolumn2 = check_isnumeric(ncolumn2, f"\nEnter The Number Of Column For Matrix [{matrix2}]: ")

        except Exception as e:
            print("something went wrong!")

        if ncolumn != nrows2:
            print("\n!cannot multiply!\nmatrix1 no of column and matrix2 no of rows must be same")
            break

        matrix1_data = []
        matrix2_data = []

        def ask_input_n(matrix, col, row, lname):
            print("\n")
            for i in range(row):
                li  = list()
                for j in range(col):
                    flag = True
                    num = input(f"Enter Value for Matrix {matrix} {i+1}{j+1}: ")    
                    while flag:
                        try:
                            li.append(float(num))
                            flag = False
                            # li.append(float(input(f"Enter Value for Matrix {matrix}-{i+1}{j+1}: ")))
                        except Exception as e:
                            flag = True
                            print("\nPlease Enter Numeric Values Only\n")
                            num = input(f"Enter Value for Matrix {matrix} {i+1}{j+1}: ")
                print()
                lname.append(li)

        ask_input_n(matrix1, ncolumn, nrows, matrix1_data)
        ask_input_n(matrix2, ncolumn2, nrows2, matrix2_data)

        def print_matrix(col, row, data, matrix):
            print(f"\n[{matrix}]")
            for i in range(row):
                print("| ", end="")
                for j in range(col):
                    print(f" {data[i][j]:g} ", end="")
                print(" |")

        def matrix_multiplication(dataM1, dataM2):
            if(ncolumn == nrows2):
                matrix_ans = list()
                for i in range(nrows):
                    multply_matrix = list()
                    for j in range(ncolumn2):
                        ans = 0
                        for k in range(nrows2):
                            ans += dataM1[i][k] * dataM2[k][j]
                        multply_matrix.append(ans)
                    matrix_ans.append(multply_matrix)
                return matrix_ans
            else:
                print("The Col1 of Row1 Must be same")
                return False

        # print_matrix(ncolumn, nrows, matrix1_data, matrix1)
        # print_matrix(ncolumn2, nrows2, matrix2_data, matrix2)

        new_matrix = matrix_multiplication(matrix1_data, matrix2_data)
        print_matrix(len(new_matrix[0]), len(new_matrix), new_matrix, "[Answer]")

        ask = input("Do You Want To Continue? y/n: ").strip(" ").lower()
        if(ask == "y"):
            pass
        elif(ask == "n"):
            go_on = False
        
    except Exception as e:
        print("\nsomething went wrong!!\n")
        print(e)

# matrix1_data = [[3,7],[4,9]]
# matrix2_data = [[6,2],[5,8]]
# matrix1_data = [[12,8,4],[3,17,14],[9,8,10]]
# matrix2_data = [[5,19,3],[6,15,9],[7, 8,16]]