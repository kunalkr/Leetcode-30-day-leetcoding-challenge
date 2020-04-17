class Solution:
    def isSafe(self, grid, i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1"
    
    def coverIsland(self, grid, i, j):
        r = [-1, 0, 0, 1]
        c = [0, 1, -1, 0]
        grid[i][j] = "2"
        
        for k in range(4):
            if self.isSafe(grid, i + r[k], j + c[k]):
                self.coverIsland(grid, i + r[k], j + c[k])
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        num_island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.coverIsland(grid, i, j)
                    num_island += 1
        
        return num_island
