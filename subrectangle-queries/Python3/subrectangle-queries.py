from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue
        return None

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

input = [
    ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle", "getValue",
     "getValue"]
    ,
    [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]], [0, 2], [0, 0, 3, 2, 5], [0, 2], [3, 1], [3, 0, 3, 2, 10], [3, 1],
     [0, 2]]
    ,
    ["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle", "getValue"]
    , [[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]], [0, 0], [0, 0, 2, 2, 100], [0, 0], [2, 2], [1, 1, 2, 2, 20], [2, 2]]
]
output = [[None, 1, None, 5, 5, None, 10, 5], [None, 1, None, 100, 100, None, 20]]
for i in range(0, len(output)):
    s = SubrectangleQueries(input[2*i + 1][0][0])
    result = [None]
    for j in range(1, len(input[2*i])):
        result.append(eval("s.{0}(*{1})".format(input[2*i][j], input[2*i + 1][j])))
    if result != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(result) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
