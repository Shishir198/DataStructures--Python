# Graph Representation

# 1) Adjacency  List  - space complexity(less than O(N^2)) is better than time complexity
                    # - effienct for sparse graph i.e, when there is a very less edges than nodes.


# 2) Adjacency Matrix -time complexity(O(1)) is better than space complexity(O(N^2))
					 # - used in dense graph
					 # - ineefiecient when graph is sparse(less no of edges than N^2 nodes)
# if there are lot of edges than nodes - adjancy matrix
# if there are very less edges  - adjancy list

# Using Adjacency Matrix
class UndirectedGraphMatrix:
	def __init__(self,n):
		self.vertices = n
		self.graph_rep =[[0]*n for i in range(n)]

	def addVertices(self):
		for i in range(self.vertices):
			 existing_row= self.graph_rep[i]
			 existing_row.append(0)

		self.vertices = self.vertices+1
		newrow = [0]*self.vertices
		newgraph = self.graph_rep
		newgraph.append(newrow)

	def addEdge(self,node1,node2,weight=1):
		self.graph_rep[node1-1][node2-1] = weight
		self.graph_rep[node2-1][node1-1] = weight

	def showGraph(self):
		n = self.vertices
		for i in range(n):
			for j in range(n):
				print(self.graph_rep[i][j] , end='\t')
			print()



# g = UndirectedGraphMatrix(4)
# g.addVertices()
# # g.showGraph()
# g.addEdge(1,2)
# g.addEdge(5,3)
# g.showGraph()


class DirectedGraphMatrix(UndirectedGraphMatrix):

	def addEdge(self,node1,node2,weight=1):
		self.graph_rep[node1-1][node2-1] = weight
		

	



# g = DirectedGraphMatrix(4)
# g.addVertices()
# g.addEdge(1,2)
# g.addEdge(5,3)
# g.showGraph()

# Using Adjacency list
class UndirectedGraphList:
	
	def __init__(self):
		self.graph_rep = {}
		

	def addVertices(self,value):
		self.graph_rep[value] = []
		

	def addEdge(self,node1,node2):
		links = self.graph_rep[node1]
		links.append(node2)
		links = self.graph_rep[node2]
		links.append(node1)
		# print(self.graph_rep)

	def showGraph(self):
		print(self.graph_rep)

# g = UndirectedGraphList()
# g.addVertices('A')
# g.addVertices('B')
# g.addVertices('E')
# g.addEdge('A','E')
# g.addEdge('A','B')
# g.addEdge('B','E')
# g.showGraph()

class DirectedGraphList(UndirectedGraphList):
	
	
	def addEdge(self,node1,node2):
		links = self.graph_rep[node1]
		links.append(node2)


g = DirectedGraphList()
g.addVertices('A')
g.addVertices('B')
g.addVertices('E')
g.addEdge('A','E')
g.addEdge('A','B')
g.addEdge('B','E')
g.showGraph()


