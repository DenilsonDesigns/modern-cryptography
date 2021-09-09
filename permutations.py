# from itertools import permutations

# my_list = [1, 2, 3, 4]

# list_of_permutations = permutations(my_list)

# cnt = 0
# for permutation in list_of_permutations:
#     cnt += 1

# print(len(my_list), cnt)

import cProfile


def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n - 1) * n


def counter(n):
    count = 0
    for i in range(n):
        count += 1
    return count


cProfile.run("counter(faculty(12))")
