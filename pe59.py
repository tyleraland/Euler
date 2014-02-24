#!/usr/bin/env python
import string
from itertools import combinations_with_replacement

# Sloppy solution.  Dumps many candidate Key,translation,sum triples
# Real solution took a little searching through the dump, but any
# further tuning of this procedure seems like overfitting

def freq_check(text):
    charCount = {x:0 for x in string.ascii_lowercase}
    for l in text:
        try: charCount[l] += 1
        except Exception: pass
    fq = sorted(charCount.items(), key=lambda tup: tup[1], reverse=True)
    top = [t[0] for t in fq[:7]]
    if ('e' in top) and ('a' in top) and ('t' in top) and ('o' in top) and ('i' in top):
        return True
    return False

f = open('pe59-input.txt').read()
nums = f.strip().split(",")

keys = combinations_with_replacement(range(97,123), 3)

#keys = ((a,b,c) for a in range(97,123) # Len = 17,576
#                for b in range(97,123)
#                for c in range(97,123))

for key in keys:
    trans = map( lambda i: chr(int(nums[i]) ^ key[i % 3]), range(0,len(nums)))
    #transt = map( lambda st: int(st), trans)
    if freq_check(trans):
        print(key)
        print(''.join(trans))
        print( reduce( lambda a,b: a+b,
                       map( lambda l: ord(l),
                            trans)))
