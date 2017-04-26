from os import listdir
from GraphNode import GraphNode

class AStar():
	"""A* search object"""
	def __init__(self):
		pass

	def generateGraph(self, graphFile, heuristicFile):
		# Open Graph file for processing
		file = open(graphFile, "r")
		lines = file.readlines()
		file.close()

		# Loop through all lines in graph file and build graph
		for i in lines:
			print(i)

			nodeInfo = i.split()

			node1 = None
			node2 = None

			# Check if first node exists, make if doesn't exist
			if nodeInfo[0] not in listdir("graph"):
				print("First Instance of " + nodeInfo[0])
				node1 = GraphNode().initial(nodeInfo[0])
				# node.save()
			else:
				node1 = GraphNode().fromFile(nodeInfo[0])
			

			# Check if second node exists, make if doesn't exist
			if nodeInfo[1] not in listdir("graph"):
				print("First Instance of " + nodeInfo[1])
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
				print("#HEURISTIC: " + i[:-1])
				print(i)

				heuristic = i.split()

				# Check if node exists
				if heuristic[0] in listdir("graph"):
					print("Passed1" + heuristic[0])
					
					node = GraphNode().fromFile(heuristic[0])
					
					node.heuristic = heuristic[1]
					node.save()

