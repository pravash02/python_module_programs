def odd_occ_in_array(A):
    n = len(A)
    if A is None or n == 0:
        return 0
    if n == 1:
        return A[0]
    result = 0
    for i in range(0, n):
        result ^= A[i]
    return result


print(odd_occ_in_array([9, 3, 9, 3, 9, 7, 9]))


def odd_occ_element(A):
    counts = {}
    for i in range(len(A)):
        if A[i] in counts:
            counts[A[i]] += 1
        else:
            counts[A[i]] = 1
    for key, value in counts.items():
        if value == 1:
            return key


print(odd_occ_element([9, 3, 9, 3, 9, 7, 9]))
