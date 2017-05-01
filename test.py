from AStar import AStar

aStar = AStar("A", "G","graph.txt", "heuristic.txt")
aStar.search()
aStar.cleanUp()

print("Done")