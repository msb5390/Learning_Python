def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        fron = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

