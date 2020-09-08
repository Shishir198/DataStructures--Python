def setRoot(treeList,value):
	if treeList[0] == None:
		treeList[0] = value
	else:
		print("Root already exist")


def setLeftChild(treeList,parent,LeftChild):

	try:
		parentIndex = treeList.index(parent)
	except : 
		print("parent Index doesnt Exist")
		return 
	
	
	parentIndex = treeList.index(parent)
	LeftChildIndex = parentIndex*2 + 1
	treeList[LeftChildIndex] = LeftChild

def setRightChild(treeList,parent,RightChild):

	try:
		parentIndex = treeList.index(parent)
	except : 
		print("parent Index doesnt Exist")
		return 
	
	
	parentIndex = treeList.index(parent)
	RightChildIndex = parentIndex*2 + 2
	treeList[RightChildIndex] = RightChild

def printTree(treeList):
	print(*treeList)


if __name__=="__main__":
	treeList = [None]*10
	setRoot(treeList,5)
	setLeftChild(treeList,5,2)
	setRightChild(treeList,5,7)
	setLeftChild(treeList,2,10)
	setRightChild(treeList,2,3)
	setLeftChild(treeList,7,1)
	setRightChild(treeList,7,3)
	printTree(treeList)

# print(treeList)