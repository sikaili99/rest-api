def squense(array,squense):
    squenseIdx = 0

    for n in array:
        if squenseIdx == len(squense):
            break 
        if n == squense[squenseIdx]:
            squenseIdx += 1
    return squenseIdx == len(squense)
