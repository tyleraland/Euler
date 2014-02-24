from math import sqrt

def facts(num, start):
    li = []
    for c in reversed(range(1,start+1)):
        if num % c == 0:
            li.append(c)
            li.append(num/c)
    return li

tri = 1
inc = 2
while len(facts(tri, int(sqrt(tri)))) < 500:
    tri += inc
    inc += 1
print("winner: " + str(tri))
