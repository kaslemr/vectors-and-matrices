class ShapeException(Exception):
    pass

def dot(vector_a, vector_b):
    def shape_checker(vector_a, vector_b):
        if shape(vector_a) != shape(vector_b):
            raise ShapeException()
    output_vector = []
    counter = -1
    for x in vector_a:
        counter += 1
        addition_num = vector_b[counter]
        new_num = x * addition_num
        output_vector.append(new_num)
    return sum(output_vector)

def magnitude(vector):
    total = 0
    for x in vector:
        total += x**2
    return total**0.5

def shape(matrix):
    row_counter = 0
    column_counter = 0
    size = []
    for row in matrix:
        row_counter += 1
        if type(row) == list:
            for x in row:
                column_counter += 1
    column_counter = int(column_counter / row_counter)
    size.append(row_counter)
    size.append(column_counter)
    if size[1] == 0:
        del size[1]
    size = tuple(size)
    return size

def vector_add(vector_a, vector_b):
    def shape_checker(vector_a, vector_b):
        if shape(matrix1) != shape(matrix2):
            raise ShapeException()
        output_vector = []
        counter = -1
        for x in vector_a:
            counter += 1
            addition_num = vector_b[counter]
            new_num = x + addition_num
            output_vector.append(new_num)
        return output_vector

def vector_sub(vector_a, vector_b):
    def shape_checker(vector_a, vector_b):
        if shape(matrix1) != shape(matrix2):
            raise ShapeException()
        output_vector = []
        counter = -1
        for x in vector_a:
            counter += 1
            subtraction_num = vector_b[counter]
            new_num = x - subtraction_num
            output_vector.append(new_num)
        return output_vector

def vector_multiply():
    return [num * scalar for num in vector]

def matrix_row():
    if row > len(matrix):
        raise ShapeException()
    if type(row) == int:
        return matrix[row]
    else:
        return "Please type an integer."

def matrix_scalar_multiply(matrix, scalar):
    new_matrix = [[col * scalar for col in row] for row in matrix]
    return new_matrix

def matrix_vector_multiply(matrix, vector):
    output_matrix = []
    for row in matrix:
        output_row = []
        counter = -1
        for column in row:
            counter += 1
            calculated_value = column * vector_a[counter]
            output_row.append(calculated_value)
        output_row = sum(output_row)
        output_matrix.append(output_row)
    return output_matrix

def matrix_matrix_multiply():
    pass

def matrix_col():
    pass
