from numpy import dot
from numpy.linalg import norm

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    res = manhattan_dist(x,y)
    return res/len(x)

def cosine_sim(x, y):
    cos_sim = dot(x, y)/(norm(x)*norm(y))
    return cos_sim

# Feel free to add more
