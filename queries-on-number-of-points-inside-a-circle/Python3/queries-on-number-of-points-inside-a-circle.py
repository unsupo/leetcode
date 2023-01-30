import math
import timeit
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # cr>sqrt((px-cx)^2+(py-cy)^2) then it's inside
        # better than O(pq)?
        def isInCircle(circle, point):
            # cx = circle[0]
            # cy = circle[1]
            # cr = circle[2]
            # px = point[0]
            # py = point[1]
            # return cr >= math.sqrt((px - cx) ** 2 + (py - cy) ** 2) # math.dist is faster
            return circle[2] >= math.dist(circle[0:2], point)

        r = []
        for circle in queries:
            point_cnt = 0
            for point in points:
                if isInCircle(circle, point):
                    point_cnt += 1
            r.append(point_cnt)
        return r

    def best(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        lengthQueries = len(queries)
        returnList = [0] * lengthQueries
        import math
        for i in range(lengthQueries):
            r = queries[i][2]
            circlePoint = [queries[i][0], queries[i][1]]
            for point in points:
                d = math.dist(circlePoint, point)
                if d > r:
                    continue
                returnList[i] += 1
        return returnList

    def my_version(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        for i in range(len(queries)):
            radius = queries[i][2]
            circle_center = queries[i][1:]

    def next_best(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = list(map(complex, *zip(*points)))
        queries = ((complex(x, y), r) for x, y, r in queries)
        return [sum(abs(p - q) <= r for p in points) for q, r in queries]


input = [[[[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]],
         [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
          [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]]]
output = [[3, 2, 2], [2, 3, 2, 4]]
for i in range(len(output)):
    r = Solution().best(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

print(timeit.timeit(stmt=lambda: Solution().best(*input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().countPoints(*input[0]), number=1_000_000))
