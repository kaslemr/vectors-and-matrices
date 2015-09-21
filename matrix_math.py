class ShapeException(Exception):
    pass


def dot():
    pass


def magnitude():
    total = 0
    for x in vector:
        total += x**2
    return total**0.5


def shape():
    pass


def vector_add():
    output_vector = []
    counter = -1
    for x in vector_a:
        counter += 1
        addition_num = vector_b[counter]
        new_num = x + addition_num
        output_vector.append(new_num)
    return output_vector

def vector_sub():
    output_vector = []
    counter = -1
    for x in vector_a:
        counter += 1
        subtraction_num = vector_b[counter]
        new_num = x - subtraction_num
        output_vector.append(new_num)
    return output_vector

def vector_sum():
    pass


def vector_multiply():
    return [num * scalar for num in vector]

def vector_mean():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
