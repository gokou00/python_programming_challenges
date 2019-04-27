def chessBoardSquaresUnderQueenAttack(a, b):
    min1 = min(a,b)
    max1 = max(a,b)
    return a*b*(a+b-2) + 2 * ( 2* (min1 - 1) * min1 * (min1 + 1)/3 + (max1-min1 -1) * (min1 - 1) * min1)
print(chessBoardSquaresUnderQueenAttack(1,1))