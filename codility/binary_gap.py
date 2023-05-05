
def binary_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))


print(binary_gap(1041))
