# A test solution

def swap_first_and_last(l):

    first, *middle, last = l

    l = [last, *middle, first]

    return l

print(swap_first_and_last([1, 2, 3]))
print(swap_first_and_last([12, 35, 9, 56, 24]))

