import random
import os
import glob
from GraphNode import GraphNode

class NodeManager():
	"""A* search object"""
	def __init__(self):
		self.LIMIT = 10
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

		# CHANGE TO PER LINE
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
			file.close()

	# Handles the nodes that are loaded in the loadedNodes list
	# Ensuring the number of nodes in list doesn't exceed the limit
	def getNode(self, node):
		for item in self.loadedNodes:
			if item.name == node:
				return item

		if len(self.loadedNodes) > self.LIMIT:
			self.loadedNodes.pop(random.randint(0, self.LIMIT - 1))
			self.loadedNodes.append(GraphNode().fromFile(node))
		else:
			self.loadedNodes.append(GraphNode().fromFile(node))

		for item in self.loadedNodes:
			if item.name == node:
				return item