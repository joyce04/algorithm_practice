# searching : 
# linear search, binary(if sorted --- log n)
# BFS, DFS

# BFS : breadth first search
# shortest path + more memory
# DFS : does path exist? + can get slow

# 1. if solution is not far from the root : BFS
# 2. if tree is very deep and solutions are rare : BFS
# 3. if tree is very wide : DFS (BFS will use large memory)
# 4. if solutions are frequent by located deep in the tree : DFS
# 5. determine whether a path exists between two nodes : DFS
# 6. finding the shortest path : BFS

# shortest path
# bellman-ford, dijkstra

# dijkstra
# 1. from root node, visit the node with the smallest distance/cost
# 2. once moved, compute the distance/cost for the neighboring nodes(sum the cost from the root node)
# 3. if the distance/cost to a node is less than the known distance, update the shortest distance
