# LeetCode 773 : Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/description/

from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = 2, 3 
        goal = "123450"  
        
        start = ''.join(str(board[i][j]) for i in range(m) for j in range(n))
        
        if start == goal:
            return 0

        q = deque([start])
        seen = set([start])

        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                s = q.popleft()
                zeroIndex = s.index('0')
                i, j = zeroIndex // n, zeroIndex % n 
                
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n:  
                        swappedIndex = x * n + y
                        t = list(s)
                        t[zeroIndex], t[swappedIndex] = t[swappedIndex], t[zeroIndex]
                        t = ''.join(t)
                        
                        if t == goal:
                            return step
                        
                        if t not in seen:
                            seen.add(t)
                            q.append(t)

        return -1