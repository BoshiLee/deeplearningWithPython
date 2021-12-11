def AND(x1, x2, theta=0.7):
    w1 = 0.5
    if x1*w1 + x2*w1 > theta:
        return 1
    else:
        return 0

print(AND(1, 0))