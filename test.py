from AStar import AStar

aStar = AStar()
aStar.cleanUp()
aStar.generateGraph("graph.txt", "heuristic.txt")

print("Done")