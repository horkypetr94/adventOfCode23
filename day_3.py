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
        print(engine_values)

        print(len(engine_values))
        total_sum = 0
        for val in engine_values:
            total_sum +=val

        print(f"Result1: {total_sum}")

def matrix_looping(matrix):
    is_engine_sign = False
    engine_values = []
    old_number = 0
    counter = 0
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_rows, num_columns = matrix.shape
    for i in range(num_rows)[1:-1]:
        for j in range(num_columns)[1:-1]:
            is_engine_sign = mini_martix_looping(i,j,matrix)
            if is_engine_sign and matrix[i,j] in numbers:
                number = find_adjacent_numbers(i, j, matrix)
                if number != old_number:
                    engine_values.append(number)
                    old_number = number
                    counter = 0
                else:
                    counter += 1
                    if counter > 3:
                        print(number)
                        print(i,j)
                        print(f"tady je {counter}")
                        print(engine_values[-5:])

    return engine_values


def mini_martix_looping(i,j,matrix):
    submatrix = matrix[i-1:i+2, j-1:j+2]
    engine_signs = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(3):
        for j in range(3):
            if submatrix[i,j] not in engine_signs:
                return True

def find_adjacent_numbers(i,j,matrix):
    row_matrix = matrix[i, j-2:j+3]
    numbers_in_row = find_numbers_in_row(matrix[i,:])
    numeric_values = random_funkce_z_chatbota(row_matrix)
    for numeric_value in numeric_values:
        if int(numeric_value) <= 999 and int(numeric_value) in numbers_in_row:
            return numeric_value
    return 0

def find_numbers_in_row(row):
    whole_numbers = []

    current_whole_number = ""
    for symbol in row:
        if symbol.isdigit():
            current_whole_number += symbol
        elif current_whole_number:
            whole_numbers.append(int(current_whole_number))
            current_whole_number = ""
    if current_whole_number:
        whole_numbers.append(int(current_whole_number))

    seen_numbers = set()

    for num in whole_numbers:
        if num in seen_numbers:
            # print(f'Two same numbers found: {num}')
            # print(whole_numbers)
            break
        seen_numbers.add(num)
    else:
        pass

    return whole_numbers

def random_funkce_z_chatbota(row):
    numeric_values=[]
    current_numeric = []
    for symbol in row:
        if symbol.isdigit():
            current_numeric.append(symbol)
        elif current_numeric:
            numeric_values.append(int(''.join(current_numeric)))
            current_numeric = []
    if current_numeric:
        numeric_values.append(int(''.join(current_numeric)))

    return numeric_values

if __name__ =="__main__":
    main()
    #missed two values
    #533347-533784
    #-437
