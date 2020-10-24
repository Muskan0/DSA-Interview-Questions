# Kartsuba Algorithm
# This algorithm is used for multiplication of numbers with large number of digits.
# It reduces the product of two large numbers into sum of three products of numbers with half the number of digits.
x=int(input("Enter the first number for multiplication"))
y=int(input("Enter the second number for multiplication"))
def k(x,y):
    n=max(len(str(x)),len(str(y)))
    if(n==1):
        return x*y
    a=x//(10**(n//2))
    b=x%(10**(n//2))
    c=y//(10**(n//2))
    d=y%(10**(n//2))
    ac=k(a,c)
    bd=k(b,d)
    abcd=k((a+b),(c+d))
    return (10**(2*(n//2)))*ac+(10**(n//2))*(abcd-ac-bd)+bd
print(x,"*",y,k(x,y))

