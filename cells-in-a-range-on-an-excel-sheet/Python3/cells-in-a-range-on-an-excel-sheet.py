from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = s.split(':')
        col1 = ord(cells[0][0])
        row1 = int(cells[0][1])
        col2 = ord(cells[1][0])
        row2 = int(cells[1][1])
        output = []
        for i in range(col2-col1+1):
            for j in range(row2-row1+1):
                output.append(chr(col1+i)+''+str(row1+j))
        return output



input = ["K1:L2", "A1:F1"]
output = [["K1", "K2", "L1", "L2"], ["A1", "B1", "C1", "D1", "E1", "F1"]]
for i in range(len(output)):
    r = Solution().cellsInRange(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
