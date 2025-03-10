'''
guide file
'''

import bisect

def result(inputfile):
    """
    compute result of exercise
    """
    list_a = []
    list_b = []
    with open(inputfile, encoding="utf-8") as f:
        for line in f:
            splits = line.strip().split('   ')
            bisect.insort(list_a, int(splits[0]))
            bisect.insort(list_b, int(splits[1]))
    result_of_function = 0
    for i, list_a_entry in enumerate(list_a):
        result_of_function += abs(list_a_entry - list_b[i])

    return result_of_function
