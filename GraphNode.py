class GraphNode():
	"""Graphnode represents each node in the graph"""

	# Using class methods to add multiple constructor functionality to python
	# Uses the data from the save method to construct a GraphNode object
	@classmethod
	def fromFile(cls, fileName):
		obj = cls()
		obj.spam

	# Using class methods to add multiple constructor functionality to python
	# Used for the first instance of the object, using arguments instead of 
	# data from a file
	@classmethod
	def initial(cls, inName, inHeuristic):
		obj = cls()
		obj.name = inName
		obj.heuristic = inHeuristic
		obj.connections = {}

	def addConnection(self, node, cost):
		self.connections[node] = cost

	def getConnections(self):
		return self.connections.keys()

	def getCost(self, nodeName):
		return self.connections[nodeName]

	# Saves the objects data as ASCII characters
	def save(self):
		file = open("/graph/" + self.name, "r")

		file.write(self.heuristic)

		for node in self.getConnections():
			file.write(node + " " + self.getCost())