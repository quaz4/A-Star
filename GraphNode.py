class GraphNode():
	"""GraphNode represents each node in the graph"""

	# Using class methods to add multiple constructor functionality to python
	# Uses the data from the save method to construct a GraphNode object
	@classmethod
	def fromFile(cls, fileName):
		obj = cls()
		obj.connections = {}
		
		# Read in each line in file
		file = open("graph/" + fileName, "r")
		lines = file.readlines()
		file.close()

		# Set name from filename as they are identical
		obj.name = fileName
		# Set heuristic then discard the line
		#print len(lines)
		#print "graph/" + fileName
		obj.heuristic = int(lines.pop(0))

		# Loop through each edge (if any)
		for line in lines:
			edgeInfo = line.split()
			obj.connections[edgeInfo[0]] = edgeInfo[1]

		return obj

	# Using class methods to add multiple constructor functionality to python
	# Used for the first instance of the object, using arguments instead of 
	# data from a file
	@classmethod
	def initial(cls, inName):
		obj = cls()
		obj.name = inName
		obj.heuristic = -1
		obj.connections = {}

		return obj

	def addConnection(self, node, cost):
		self.connections[node] = cost

	def getConnections(self):
		return self.connections.keys()

	def getCost(self, nodeName):
		return self.connections[nodeName]

	# Saves the objects data as ASCII characters
	def save(self):
		file = open("graph/" + self.name, "w+")
		#print "Opened file to save"

		file.write(str(self.heuristic)  + "\n")

		#print "Written heuristic value"

		for node in self.getConnections():
			file.write(node + " " + self.getCost(node) + "\n")
			#print "Writing connection data"

		#print("saved")