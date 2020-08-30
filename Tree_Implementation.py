from collections import deque
class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self,node):
		if self.root == None:
			self.root = node
		else:
			data = node.value
			currentNode = self.root
			while  True:
				
				if data < currentNode.value:
					# left
					if currentNode.leftNode==None:
						currentNode.leftNode = node
						print(data,"Added to the left of ",currentNode.value)
						break
					else:
						currentNode = currentNode.leftNode
				# right
				elif data > currentNode.value:
					if currentNode.rightNode==None:
						currentNode.rightNode = node
						print(data,"Added to the right of",currentNode.value)
						break
					else:
						currentNode = currentNode.rightNode
				else:
					print("NO Duplicate Values Allowed")
					break

	def BreadthFirstSearch(self):
		stack = []
		queue = deque([])
		queue.append(self.root)
		# stack = []
		# queue = [8]
		# target - [8,3,10,1,6,14,4,7,13]
		while len(queue)>0:
			currentNode = queue[0]
			stack.append(currentNode.value)  # 8 3 10 1 6 14 4 7 13
			if currentNode.leftNode !=None:
				queue.append(currentNode.leftNode)
			if currentNode.rightNode !=None:
				queue.append(currentNode.rightNode)
			# queue = [13]
			queue.popleft()
			# queue = []
		print(stack)

	

	def InOrder(self,node, list):
	  if node.leftNode:
	  	self.InOrder(node.leftNode,list)

	  list.append(node.value)

	  if node.rightNode:
	  	self.InOrder(node.rightNode,list)

	  return list

	def traverseInOrder(self):

		return self.InOrder(self.root, [])

	def PreOrder(self,node, list):

	  list.append(node.value)
	  if node.leftNode:
	  	self.PreOrder(node.leftNode,list)

	  if node.rightNode:
	  	self.PreOrder(node.rightNode,list)

	  return list

	
	def traversePreOrder(self):

		return self.PreOrder(self.root, [])


	def PostOrder(self,node, list):

	  
	  if node.leftNode:
	  	self.PostOrder(node.leftNode,list)

	  

	  if node.rightNode:
	  	self.PostOrder(node.rightNode,list)


	  list.append(node.value)
	  return list

	
	def traversePostOrder(self):

		return self.PostOrder(self.root, [])


class Node:
	def __init__(self,value):
		self.value = value
		self.leftNode = None
		self.rightNode = None


tree = BinarySearchTree()
tree.insert(Node(9))
tree.insert(Node(2))
tree.insert(Node(3))
tree.insert(Node(73))
tree.insert(Node(108))
tree.insert(Node(10))
tree.insert(Node(1))
# tree.BreadthFirstSearch()
print(tree.traverseInOrder())
print(tree.traversePreOrder())
print(tree.traversePostOrder())