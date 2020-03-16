def transpose(matrix): return [' '.join([row.split(' ') for row in matrix][i][j]
                                        for i in range(len(matrix))) for j in range(len(matrix))]


print('transpose:', transpose(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))


def flatten(l):
    for element in l:
        if isinstance(element, list):
            for nested_element in flatten(element):
                yield nested_element
        else:
            yield element


print('flatten:', list(flatten([[1, 2, ["a", 4, "b", 5, 5, 5]],
                                [4, 5, 6], 7, [[9, [123, [[123]]]], 10]])))


def last_col(filename):
    with open(filename, 'r') as f:
        return sum(int(line.split(' ')[-1]) for line in f)


print('bytes in last col:', last_col('test.txt'))


def quicksort(l):
    if len(l) in (0, 1):
        return l
    first, rest = l[0], l[1:]
    return quicksort([x for x in rest if x < first]) + [first] + quicksort([x for x in rest if x >= first])


print('quicksort:', quicksort([1, 5, 123, 0, -3, 2]))


def subsets(l):
    if len(l) == 0:
        return [[]]
    first, rest = l[0], l[1:]
    return subsets(rest) + list(map(lambda ss: [first, *ss], subsets(rest)))


print('subsets:', subsets([1, 2, 3]))
