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
        total_sum = sum([value if value is not None else 0 for value in engine_values])

        print(f"Result1: {total_sum}")

def matrix_looping(matrix):
    is_engine_sign = False
    engine_values = []
    old_number = 0
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num_rows, num_columns = matrix.shape
    for i in range(num_rows)[1:-1]:
        for j in range(num_columns)[1:-1]:
            is_engine_sign = mini_martix_looping(i,j,matrix)
            if is_engine_sign and matrix[i,j] in numbers:
                number = find_adjacent_numbers(i,j, matrix)
                if number != old_number:
                    engine_values.append(number)
                    old_number = number
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
    numeric_value = int(''.join([symbol for symbol in row_matrix if symbol.isdigit()]))
    if numeric_value <= 999:
        return numeric_value


if __name__ =="__main__":
    main()