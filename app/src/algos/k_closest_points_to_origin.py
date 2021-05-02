from heapq import heappush, heappushpop
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = self.get_dist(x, y)

            if len(pq) < k:
                heappush(pq, (dist, point))
            else:
                heappushpop(pq, (dist, point))
        return [point for (dist, point) in pq]

    def get_dist(self, x, y):
        return sqrt(x*x + y*y)

points = [[3,3],[5,-1],[-2,4]]
close = Solution().kClosest(points, 2)
print(close)