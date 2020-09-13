from math import ceil,log2
givenArr = [2,5,1,4,9,3]


def BuildSegmentTree(givenArr,DesiredArray,start=0,end=len(givenArr)-1,desiredIndex=0):  #Time Complexity = O(N)

	if start == end:
		DesiredArray[desiredIndex] = givenArr[start]
		return 

	mid = (start+end)//2
	# print("mid=",mid)
	# print("BuildlEFTSegmentTree of ",start , mid ,"stroing in",2*desiredIndex)
	BuildSegmentTree(givenArr,DesiredArray,start,mid,2*desiredIndex+1)
	# print("BuildRIGHTSegmentTree of ",mid+1 , end ,"stroing in",2*desiredIndex+1)

	BuildSegmentTree(givenArr,DesiredArray,mid+1,end,2*desiredIndex + 2)
	DesiredArray[desiredIndex] = min(DesiredArray[2*desiredIndex +1],DesiredArray[2*desiredIndex+2])
	# print("DesiredArray=",DesiredArray)
	
x = (int)(ceil(log2(len(givenArr))));   
max_size = 2 * (int)(2**x) - 1

DesiredArray = [None]*max_size
# DesiredArray=[0]*(2*len(givenArr)-1)
# print("Building tree from",0 , len(givenArr)-1)
BuildSegmentTree(givenArr,DesiredArray)
print(DesiredArray)

