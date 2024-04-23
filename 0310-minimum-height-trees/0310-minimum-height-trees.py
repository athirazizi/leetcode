class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # time complexity: O(n)
        
        if n == 1:
            return [0]
        
        adjacencyList = defaultdict(list)
        
        # link each node to neighbour
        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        edgeCount = {}
        leaves = deque()
        
        for src, neighbours in adjacencyList.items():
            # find all leaf nodes
            if len(neighbours) == 1:
                leaves.append(src)
            edgeCount[src] = len(neighbours)              
        
        while leaves:
            # maximum number of mhts
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neigh in adjacencyList[node]:
                    edgeCount[neigh] -= 1
                    if edgeCount[neigh] == 1:
                        leaves.append(neigh)
                    
        

            