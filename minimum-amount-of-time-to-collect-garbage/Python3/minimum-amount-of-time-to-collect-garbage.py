import timeit
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0
        # this will record the last visited house for each garbage type
        # this hard codes to 3 garbage types
        last_house_truck = {'M': 0, 'P': 0, 'G': 0}
        for house in range(len(garbage)):
            # time to collect all garbage at a house is length of string doesn't matter garbage type
            time += len(garbage[house])
            # plus the time to move to the next house for every truck
            # this will be too much since every truck doesn't need to go to the last house
            # all trucks start at house 0 so there is no travel time there
            if house > 0:
                for garbage_type in set(garbage[house]):
                    last_house_truck[garbage_type] = house
                time += len(last_house_truck) * travel[house - 1]
        # now i must remove truck times based on the last house they visited
        for last_house in last_house_truck.values():
            for times in range(len(travel) - last_house):
                time -= travel[len(travel) - times - 1]
        return time


    def best_garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage) # number of houses
        # trick here is it starts at the end so you already know the last house with each garbage type
        i, m, g, p = n - 1, -1, -1, -1 # house index, metal, glass, paper

        while (m == -1 or g == -1 or p == -1) and i > 0:
            # find out the last house with each garbage type
            if "M" in garbage[i] and m < 0:
                m = i
            if "G" in garbage[i] and g < 0:
                g = i
            if "P" in garbage[i] and p < 0:
                p = i

            i -= 1

        # sum up the length of each string in each house
        total = sum([len(g) for g in garbage])
        # using the last house above sum up the distances
        total += sum(travel[:m]) if m != -1 else 0
        total += sum(travel[:p]) if p != -1 else 0
        total += sum(travel[:g]) if g != -1 else 0

        return total


input = [[["G", "P", "GP", "GG"], [2, 4, 3]], [["MMM", "PGM", "GP"], [3, 10]]]
output = [21, 37]
for i in range(len(output)):
    r = Solution().garbageCollection(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))


print(timeit.timeit(stmt=lambda: Solution().garbageCollection(*input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().best_garbageCollection(*input[0]), number=1_000_000))
# 1.460963667021133 # mine
# 0.8912613749853335 # best