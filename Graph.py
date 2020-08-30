# Graph Representation

# 1) Adjacency  List  - space complexity(less than O(N^2)) is better than time complexity
                    # - effienct for sparse graph i.e, when there is a very less edges than nodes.


# 2) Adjacency Matrix -time complexity(O(1)) is better than space complexity(O(N^2))
					 # - used in dense graph
					 # - ineefiecient when graph is sparse(less no of edges than N^2 nodes)
# if there are lot of edges than nodes - adjancy matrix
# if there are very less edges  - adjancy list

# Adjacency list


class UndirectedGraphList:
	
	def __init__(self):
		self.graph_rep = {}
		# print(self.graph_rep)

	def addVertices(self,value):
		self.graph_rep[value] = []
		# print(self.graph_rep)

	def addEdge(self,node1,node2):
		links = self.graph_rep[node1]
		links.append(node2)
		links = self.graph_rep[node2]
		links.append(node1)
		# print(self.graph_rep)

	def showGraph(self):
		print(self.graph_rep)

g = UndirectedGraphList()
g.addVertices('A')
g.addVertices('B')
g.addVertices('E')
g.addEdge('A','E')
g.addEdge('A','B')
g.addEdge('B','E')
g.showGraph()

class DirectedGraphList:
	
	def __init__(self):
		self.graph_rep = {}
		# print(self.graph_rep)

	def addVertices(self,value):
		self.graph_rep[value] = []
		# print(self.graph_rep)

	def addEdge(self,node1,node2):
		links = self.graph_rep[node1]
		links.append(node2)
		

	def showGraph(self):
		print(self.graph_rep)


g = DirectedGraphList()
g.addVertices('A')
g.addVertices('B')
g.addVertices('E')
g.addEdge('A','E')
g.addEdge('A','B')
g.addEdge('B','E')
g.showGraph()



