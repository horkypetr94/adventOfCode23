import numpy as np

def main():
    with open("data/3") as f:
        lines = f.readlines()
        map_list = []
        for line in lines:
            row = [symbol for symbol in line.strip()]
            map_list.append(row)
        matrix = np.array(map_list)
        #add padding for sliding window
        matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=".")
        engine_values = matrix_looping(matrix)
        total_sum = 0
        for val in engine_values:
            total_sum +=val

        print(f"Result1: {total_sum}")

def matrix_looping(matrix):
    engine_values = []
    string_number = ""
    list_of_numbers = []
    is_engine_sign_list = []
    num_rows, num_columns = matrix.shape
    for i in range(num_rows)[1:-1]:
        for j in range(num_columns)[1:-1]:
            symbol = matrix[i, j]

            if symbol.isdigit():
                string_number += symbol
                is_engine_sign_list.append(check_for_sign(i, j, matrix))

            else:
                try:
                    if True in is_engine_sign_list:
                        list_of_numbers.append(int(string_number))
                        string_number = ""
                        is_engine_sign_list = []
                    else:
                        string_number = ""
                except:
                    string_number = ""
    return list_of_numbers



def check_for_sign(i, j, matrix):
    submatrix = matrix[i-1:i+2, j-1:j+2]
    engine_signs = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(3):
        for j in range(3):
            if submatrix[i,j] not in engine_signs:
                return True
    return False

if __name__ =="__main__":
    main()
    #missed two values
    #533347-533784
    #-437
