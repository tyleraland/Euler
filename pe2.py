# Problem 2
# Find the largest palindrome made from the product of two 3-digit numbers

def is_pal(num):
  snum = str(num)
  for i in range(0,len(snum)/2):
    if snum[i] != snum[-i-1]:
      return False
  return True

max = 0
for m in range(100, 999):
  for n in range(100, m+1):
    if is_pal(m*n) and m*n > max:
      max = m*n
print(max)
