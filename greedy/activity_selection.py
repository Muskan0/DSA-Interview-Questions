# https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1/?ref=self#

def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    l=[]
    for i in range(n):
        l.append([start[i],end[i]])
    # Sort jobs according to finish time
    l.sort(key= lambda x : x[1])
    ans=1
    m=l[0][1]
    for i in range(1,n):
        # If this activity has start time greater than or 
        # equal to the finish time of previously selected 
        # activity, then select it 
        if l[i][0]>=m:
            ans+=1
            m=l[i][1]
            
    return ans
