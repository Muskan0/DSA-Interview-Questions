# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#

#User function Template for python3
def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    for i in range(n):
        Items[i]=[Items[i],Items[i].value/Items[i].weight]
    i=0
    Items.sort(reverse= True, key= lambda x: x[1])
    ans=0
    while W>0:
        if Items[i][0].weight<=W:
            ans+=Items[i][0].value
            W-=Items[i][0].weight
        elif Items[i][0].weight>W:
            ans+=Items[i][0].value*(W/Items[i][0].weight)
            break
        i+=1
    return ans
