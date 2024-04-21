from collections import defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # Create an adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize a set to keep track of visited nodes
        visited = set()

        # Define the DFS function
        def dfs(node):
            # If the node is the destination, return True
            if node == destination:
                return True

            # Mark the node as visited
            visited.add(node)

            # Visit all the neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        # Start the DFS from the source node
        return dfs(source)
