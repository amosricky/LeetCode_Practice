def solution(A, B):
    # write your code in Python 3.6
    if A < 1 or B < 1:
        return 0

    longStick = A if A > B else B
    shortStick = B if B < A else A
    maxStick = 0

    for i in range(2, 5):
        if i == 4:
            if longStick//4 > 0:
                temp = longStick//4
                maxStick = max(maxStick, temp)
        if i == 3:
            slipStick = longStick//3
            temp = min(slipStick, shortStick)
            maxStick = max(maxStick, temp)
        if i == 2:
            temp = shortStick//2
            maxStick = max(maxStick, temp)

    return maxStick


