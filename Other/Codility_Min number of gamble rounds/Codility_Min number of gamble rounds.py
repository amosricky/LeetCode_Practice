def solution(N, K):
    # write your code in Python 3.6
    rounds = 0
    betAll = K

    chips = N

    while chips > 1:
        if chips % 2 == 0 and betAll > 0:
            chips = chips//2
            betAll -= 1
        else:
            chips -= 1
        rounds += 1

    return rounds