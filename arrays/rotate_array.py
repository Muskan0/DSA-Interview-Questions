# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0#

'''
Approach:
Ex: 1 2 3 4 5 to rotate by 2 elements
Step 1: Reverse first d elements.
--> 2 1 3 4 5
Step 2: Reverse next n-d elements
--> 2 1 5 4 3
Step 3: Reverse the array.
--> 3 4 5 1 2 is the answer.

'''
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
  
for _ in range(int(input())):
    N, D = map(int, input().split())
    arr = list(map(int, input().split()))
    D = D % N

    arr = reverse(arr, 0, D-1)
    arr = reverse(arr, D, N-1)
    arr = reverse(arr, 0, N-1)
    
    for i in arr:
        print(i, end=" ")
    print()
    
# Time Complexity: O(n)
# Space Complexity: O(1)    
