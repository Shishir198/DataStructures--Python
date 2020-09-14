from math import ceil,log2
givenArr = [1,3,5,7,9,11]


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
	DesiredArray[desiredIndex] = DesiredArray[2*desiredIndex +1] + DesiredArray[2*desiredIndex+2]
	# print("DesiredArray=",DesiredArray)
	
def updateValueAt(array,node,amount):
	try:
		index = array.index(node)
		while index>=0:
			array[index] = array[index]+amount
			index = (index-1)//2
	except:
		print("Value",node,"Doesnt Exist in the array")


x = (int)(ceil(log2(len(givenArr))));   
max_size = 2 * (int)(2**x) - 1

DesiredArray = [None]*max_size
# print("Building tree from",0 , len(givenArr)-1)
BuildSegmentTree(givenArr,DesiredArray)
print(DesiredArray)
updateValueAt(DesiredArray,1,2)
print(DesiredArray)
