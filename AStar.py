import os
import glob
from GraphNode import GraphNode

class AStar():
	"""A* search object"""
	def __init__(self):
		self.graphNodesCount = 0
		self.loadedNodes = []
		self.treeCount = 0
		self.frontierCount = 0
		self.frontier = []

	def generateGraph(self, graphFile, heuristicFile):
		# Open Graph file for processing
		file = open(graphFile, "r")
		lines = file.readlines()
		file.close()

		# Loop through all lines in graph file and build graph
		for i in lines:
			#print(i)

			nodeInfo = i.split()

			node1 = None
			node2 = None

			# Check if first node exists, make if doesn't exist
			if nodeInfo[0] not in os.listdir("graph"):
				#print("First Instance of " + nodeInfo[0])
				node1 = GraphNode().initial(nodeInfo[0])
				# node.save()
			else:
				node1 = GraphNode().fromFile(nodeInfo[0])
			

			# Check if second node exists, make if doesn't exist
			if nodeInfo[1] not in os.listdir("graph"):
				#print("First Instance of " + nodeInfo[1])
				node2 = GraphNode().initial(nodeInfo[1])
				# node.save()
			else:
				node2 = GraphNode().fromFile(nodeInfo[1])

			# Add edges
			node1.addConnection(nodeInfo[1], nodeInfo[2])
			node2.addConnection(nodeInfo[0], nodeInfo[2])

			node1.save()
			node2.save()

		# If a heuristic file was included, process it
		if heuristicFile != None:
			file = open(heuristicFile, "r")
			lines = file.readlines()
			file.close()

			# Loop through all lines in Heuristic file and add values to graph
			for i in lines:
				#print("#HEURISTIC: " + i[:-1])
				#print(i)

				heuristic = i.split()

				# Check if node exists
				if heuristic[0] in os.listdir("graph"):
					#print("Passed1" + heuristic[0])
					
					node = GraphNode().fromFile(heuristic[0])
					
					node.heuristic = heuristic[1]
					node.save()

	# Remove all files previously generated in 'graph' directory
	def cleanUp(self):
		print "Cleanup"
		for file in glob.glob("graph/*"):
			print("FILE REMOVED: " + file)
			os.remove(file)

	def search(self, root, goal):
		# Initialise frontier by adding root value
		wrapper = []
		wrapper.append(0)
		wrapper.append(GraphNode().fromFile(root))
		self.frontier.append(wrapper)

		while True:
			self.updateFrontier()
			break

	def updateFrontier(self):
		sucessor = self.frontier[0]



		#for child in sucessor.connections.
		#	pass
		'''
		copy = list(self.frontier)

		for node in copy:
			# TODO that 15 is subject to change later I just needed a number
			if len(self.frontier) > 15:
				self.frontier.pop()

			self.frontier.
		'''

	
	# Handles the nodes that are loaded in the loadedNodes list
	# Ensuring the number of nodes in list doesn't exceed the limit
	def loadNode(self, node):
		#for graphNode in self.loadedNodes:
			#if graphNode.name == node:
			#	return graphNode
		
		if len(self.loadedNodes) > 6:
			self.loadedNodes.pop(0)
			self.loadedNodes.append(GraphNode().fromFile(node))
		else:
			self.loadedNodes.append(GraphNode().fromFile(node))

	def addFrontier(self, path, node, total):
		file = open("frontier/" + total + "_" + node, "w+")
		file.write(path)

	def removeFrontier(self, node, total):
		os.remove("frontier/" + total + "_" + node)