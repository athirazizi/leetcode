class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    bottom, right = i, j
                    while bottom < m and land[bottom][j] == 1:
                        bottom += 1
                    while right < n and land[i][right] == 1:
                        right += 1
                    for x in range(i, bottom):
                        for y in range(j, right):
                            land[x][y] = 0
                    res.append([i, j, bottom - 1, right - 1])
        return res
 
