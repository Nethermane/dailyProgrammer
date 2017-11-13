def firstCopy(inp):
    lis = []
    count = 0
    for i in inp:
        if i in lis:
            return count
        lis.append(i)
        count+=1
    return None
