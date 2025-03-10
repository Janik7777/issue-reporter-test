import bisect

def result(inputfile):
    list_a = []
    list_b = []
    with open(inputfile) as f:
        for line in f:
            splits = line.strip().split('   ')
            bisect.insort(list_a, int(splits[0]))
            bisect.insort(list_b, int(splits[1]))
        
    result = 0
    for i in range(len(list_a)):
        result += abs(list_a[i] - list_b[i])
        
    return result