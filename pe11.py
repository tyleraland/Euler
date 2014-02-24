import itertools

def right(starti, endi, startj, endj):
    # Generate list of starting indices
    ins = tuple(itertools.product(range(starti,endi+1), range(startj,endj+1)))
    # Foreach index-pair, collect it and its neighbors in a list
    x = map( lambda t: [g[t[0]][j] for j in range(t[1],t[1]+4)], ins)
    # list of quads -> list of products -> max of list of products
    return max( map( lambda l: reduce( lambda a1,a2: a1*a2, l), x))

def down(starti, endi, startj, endj):
    ins = tuple(itertools.product(range(starti,endi+1), range(startj,endj+1)))
    x = map( lambda t: [g[i][t[1]] for i in range(t[0],t[0]+4)], ins)
    return max( map( lambda l: reduce( lambda a1,a2: a1*a2, l), x))

def ldiag(starti, endi, startj, endj):
    ins = tuple(itertools.product(range(starti,endi+1), range(startj,endj+1)))
    x = map( lambda t: [g[t[0]+k][t[1]-k] for k in range(0,4)], ins)
    return max( map( lambda l: reduce( lambda a1,a2: a1*a2, l), x))

def rdiag(starti, endi, startj, endj):
    ins = tuple(itertools.product(range(starti,endi+1), range(startj,endj+1)))
    x = map( lambda t: [g[t[0]+k][t[1]+k] for k in range(0,4)], ins)
    return max( map( lambda l: reduce( lambda a1,a2: a1*a2, l), x))

file = open('pe11-input')
g = [[int(num) for num in line.strip().split(' ')] for line in file]

print(max( [down(0,16,0,19),
            right(0,19,0,16),
            ldiag(0,16,3,19),
            rdiag(0,16,0,16)]))
