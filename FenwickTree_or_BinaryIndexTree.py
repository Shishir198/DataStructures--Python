
def getsum(BITTree,i):
    #to get Parent
    # - 2's complement of number
    # - AND with original number
    # - Subtract with original number
    s = 0 
    i = i+1
    while i > 0: 
        s += BITTree[i] 
        i -= i & (-i) 
    return s 

def updatebit(BITTree , n , i ,v): 
    # to get next element 
    # - 2's complement of number
    # - AND with original number
    # - Add to original number
    i += 1
    while i <= n: 
        BITTree[i] += v 
        i += i & (-i) 

def construct(arr, n): 
    BITTree = [0]*(n+1) 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
  
    for i in range(1,n+1): 
        print(BITTree[i]) 
    return BITTree 

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
BITTree = construct(freq,len(freq)) 
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))) 
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+
                    " after update is " + str(getsum(BITTree,5))) 
  