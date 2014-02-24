import multiprocessing
import numpy as np

top = 1000000

def collatz(num):
    med = num
    cnt = 0
    while med > 1:
        cnt += 1
        if med % 2 == 0:
            med /= 2
        else:
            med = med*3 + 1
    return(cnt)

cnt_li = map( lambda n: collatz(n), range(top))
i = np.argmax(cnt_li)
print(i)
