# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m/0#

for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    low=1
    high=m
    guess=(low+high)/2
    epsilon=0.0000001
    while abs(guess**n-m)>=epsilon:
        if guess**n>m:
            high=guess
        else:
            low=guess
        guess=(low+high)/2
    #print(round(guess))
    if m==round(guess)**n:
        print(int(round(guess)))
    else:
        print(-1)
