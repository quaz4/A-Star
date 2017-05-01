import os
import glob
from GraphNode import GraphNode

from FrontierManager import FrontierManager

class AStar():
	"""A* search object"""
	def __init__(self, root, goal, graphFile, heuristicFile):
		self.frontierManager = FrontierManager(root, goal, graphFile, heuristicFile)

	# Remove all files previously generated in 'graph' directory
	def cleanUp(self):
		print "Cleanup"
		for file in glob.glob("graph/*"):
			print("FILE REMOVED: " + file)
			os.remove(file)

	# Redo
	def search(self):
		while self.frontierManager.addFrontierFile(self.frontierManager.findBestNode()) > 0	:
			print "SEARCHING"

		print "############################################"

		while self.frontierManager.addFrontierFile(self.frontierManager.findAlternatives(50)) != -1:
			print "ALT"

		print "############################################"