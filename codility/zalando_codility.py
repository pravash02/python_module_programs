def solution(A, X):
    """
    The code you provided implements a binary search algorithm to find the index of an element X in a sorted list A.
    However, there is a bug in the algorithm that causes it to fail for certain inputs.
    The bug is in the line 'l = m'. This line sets the left boundary of the search range to the current middle element.
    However, if the middle element is not equal to X, this can cause the algorithm to skip over the correct index for X.
    Specifically, if the correct index for X is between the current middle index and the previous middle index,
    the algorithm will fail to find it.
    """
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m
    if A[l] == X:
        return l
    return -1


# sol
def solution_correct(A, X):
    """
    The main difference between the original code and the modified code is the comparison in the if statement inside
    the while loop. In the original code, the comparison is if A[m] > X, which checks whether the middle element is
    greater than the target value. In the modified code, the comparison is if A[m] < X, which checks whether the middle
    element is less than the target value. This difference in comparison affects how the search range is updated in
    each iteration of the while loop.

    In the modified code, if the middle element is less than the target value, the left boundary is updated to m + 1,
    effectively eliminating the lower half of the search range. If the middle element is greater than or equal to the
    target value, the right boundary is updated to m, effectively eliminating the upper half of the search range.
    This ensures that the target value is always contained within the remaining search range.
    """
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] < X:
            l = m + 1
        else:
            r = m
    if A[l] == X:
        return l
    return -1


# print(([1, 2, 5, 9, 9], 5))


def solution_skyline_brush_count(A):
    """
    A brush stroke starts whenever the height increases going from left - right nd ends when it decreases.
    You only need to look at when it increases, because if you just count the starting points of each stroke you will
    have the stroke count. Instead of looping over the height levels in an inner loop, just subtract one height level
    from the previous to get the difference.
    """
    brush_count = 0
    prev_bulding = 0
    for i in range(len(A)):
        if A[i] > prev_bulding:
            brush_count = brush_count + A[i] - prev_bulding
        prev_bulding = A[i]

    return brush_count


print(solution_skyline_brush_count([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))


def solution_max_emp_attendee(E):
    """
    we need to consider all possible pairs of two days during which the training can take place. For each pair,
    we will count the number of employees who are available on at least one of these two days.
    Finally, we will return the maximum count
    Iterate over all possible pairs of two days from the next 10 days.
    For each pair of two days, iterate over all employees and count the number of employees who are available on
    at least one of these two days.
    """
    emp_lst_len = len(E)
    max_cnt = 0

    for day1 in range(9):
        for day2 in range(day1 + 1, 10):
            cnt = 0

            for emp in range(emp_lst_len):
                if str(day1) in E[emp] or str(day2) in E[emp]:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
    return max_cnt


print(solution_max_emp_attendee(['039', '4', '14', '32', '', '34', '7']))