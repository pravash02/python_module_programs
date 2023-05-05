def rotate_array(A, K):
    temp_array = [0] * len(A)

    for index in range(len(A)):
        new_index = (index + K) % len(A)  # new position
        temp_array[new_index] = A[index]  # set value

    return temp_array


print(rotate_array([1, 2, 3, 4], 2))


def rotate_arr(A, K):
    counter = 0
    for i in range(len(A)):
        A.insert(0, A[-1])
        del A[-1]
        counter += 1

        if counter == K:
            return A


print(rotate_arr([1, 2, 3, 4], 2))
