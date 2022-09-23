def euclidean_dist(x, y):
    if x == None or y == None:
        return 0
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    res = manhattan_dist(x,y)
    return res/len(x)

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    res = sum([i*j for (i, j) in zip(x, y)])

    zerox = [0] * len(x)
    zeroy = [0] * len(y)

    if (euclidean_dist(x,zerox) + euclidean_dist(y,zeroy)) == 0:
        return 0

    cos_sim = res / (euclidean_dist(x,zerox) * euclidean_dist(y,zeroy))
    return cos_sim

# Feel free to add more
