import numpy as np

# creating arrays

if __name__ == "__main__":
    # 1d array of numbers
    numbers = np.arange(8, 34)
    numbers = np.array([i for i in range(8, 34)])

    arr1 = np.array([i for i in range(8, 20)])
    arr2 = np.array([i for i in range(20, 34)])
    numbers = np.concatenate((arr1, arr2))

    # 2d random array
    random_2d = np.random.random((4, 4, 4))

    random_2d = np.linspace(0., 1., 8)
    np.random.shuffle(random_2d)
    random_2d.reshape((2, 2, 2))

    # 2d diagonal matrix
    diag = np.eye(4) * 2
    diag = np.diag([2, 2, 2, 2])

    A = np.ones((2, 2)) * 2
    B = np.zeros((2, 2))
    diag = np.block([[A, B], [B, A]])

    arr1 = np.array([2, 0, 0, 0])
    arr2 = np.array([0, 2, 0, 0])
    diag = np.stack((arr1, arr2, np.flip(arr2), np.flip(arr1)), axis=1)


# matrix multiplication

def matrix_multiplication(m1, m2):
    result = m1 @ m2
    return result


# multiplication check

def multiplication_check(matrix_list):
    previous_matrix_shape = matrix_list[0].shape
    for i in range(1, len(matrix_list)):
        next_matrix_shape = matrix_list[i].shape
        if previous_matrix_shape[1] != next_matrix_shape[0]:
            return False
        previous_matrix_shape = (matrix_list[i-1].shape[0], matrix_list[i].shape[1])
    return True


# multiply matrices

def multiply_matrices(matrix_list):
    result = matrix_list[0]
    if multiplication_check(matrix_list):
        return np.linalg.multi_dot(matrix_list)
    else:
        return None


# 2D distance
# we can calculate distance using Pythagorean theorem but the easier way is using l2 norm which we will use in the next task

def compute_2d_distance(point1, point2):
    dist = ((point2 - point1)**2).sum()**0.5
    return dist


# multidimensional distance
# (tnx to https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy)

def compute_multidimensional_distance(arr1, arr2):
    dist = np.linalg.norm(arr1 - arr2)
    return dist


# pairwise distances
# (tnx to https://stackoverflow.com/questions/43367001/how-to-calculate-euclidean-distance-between-pair-of-rows-of-a-numpy-array)

def compute_pair_distances(arr):
    arr_turned = arr.reshape(arr.shape[0], 1, arr.shape[1])
    result = np.sqrt(np.einsum('ijk, ijk->ij', arr - arr_turned, arr - arr_turned))
    return result




