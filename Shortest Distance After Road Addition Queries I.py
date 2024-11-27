# LeetCode 3243 : Shortest Distance After Road Addition Queries I
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        madj = {i: [i + 1] for i in range(n - 1)}
        madj[n - 1] = []
        
        def bfs():
            far = [float('inf')] * n
            far[0] = 0
            line = deque([0])
            
            while line:
                u = line.popleft()
                for v in madj[u]:
                    if far[u] + 1 < far[v]:
                        far[v] = far[u] + 1
                        line.append(v)
            
            return far[n - 1]
        
        riz = []
        
        for u, v in queries:
            if v not in madj[u]:
                madj[u].append(v)
            riz.append(bfs())
        
        return riz