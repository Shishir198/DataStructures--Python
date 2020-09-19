array = [50,30,20,15,10,8,16]

# max heap
def insert(arr,value): #----------------> O(log N)
	arr.append(value)
	pos = len(array)-1
	# print("pos=",pos)
	parentindex = (pos-1)//2 
	# print("parentindex=",parentindex)
	while arr[pos] > arr[parentindex] and parentindex>=0:
		# print("swapping",arr[pos],arr[parentindex])
		arr[pos],arr[parentindex] = arr[parentindex] , arr[pos]
		# print("array",arr)
		pos = parentindex
		# print("newpos=",pos)
		parentindex = (pos-1)//2 
		# print("newparentindex=",parentindex)


def pop(arr): #----------------> O(log N)
	arr[0],arr[-1] = arr[-1],arr[0]
	# print("swipe",array)
	finalLen = len(arr)-1
	pos = 0
	lchildindex = 2*pos+1
	rchildindex = 2*pos+2

	while lchildindex <= finalLen and rchildindex <= finalLen and arr[pos] < max(arr[lchildindex],arr[rchildindex]):
		maxElem = max(arr[lchildindex],arr[rchildindex])
		# print("maxElem",maxElem)
		if arr[lchildindex] == maxElem :
			maxI = lchildindex
		else:
			maxI = rchildindex
		# print("maxI",maxI)
		# print("swapping",arr[pos],arr[maxI])
		arr[pos],arr[maxI] = arr[maxI],arr[pos]
		# print(array)
		pos = maxI
		lchildindex = 2*pos+1
		rchildindex = 2*pos+2
		# print(pos,lchildindex,rchildindex)


insert(array,60)
print(array)
pop(array)
print(array)
pop(array)
print(array)




