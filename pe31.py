change = 200
#coinage = [1, 2, 5, 10, 20, 50, 100, 200]
coinage = [1,5]

def make_change(amount,coini):
    ways = 0
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    else:
        for coin in range(0,coini):
            if (make_change(amount - coinage[-coin-1], coini-coin)) > 0:
                print("amount: " + str(amount - coinage[-coin-1]))
                print("coini : " + str(coini-coin))
            ways += make_change(amount - coinage[-coin-1], coini-coin)
            
    return ways

print(make_change(10, len(coinage)))

# -1 -2 -3

5,5
5,1,1,1,1,1
1,1,1,1,1,1,1,1,1,1

# [1, 5]
# make_change(10, 2)
# ways = make_change(10 - coinage[-0-1], 2-0) + make_change(10 - coinage[-1-1], 2-1)
# make_change(10 - 5, 2) =
#   make_change(5 - 5, 2) = 1
#   make_change(5 - 1, 1) = ... 1
# make_change(9, 1)
#   make_change
# make
# -> make_change(0, 2) + make_change(5, 1) + make_change(9, 0)
# -> 1 + (make_change(0, 1) + make_change(4, 1)) + (make_change_
