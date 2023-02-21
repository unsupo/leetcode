import timeit
from typing import List


class OrderedStream:
    size: int = 0
    arr: List[str] = []
    ptr: int = 1

    def __init__(self, n: int):
        self.size = n
        self.arr = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        rtn = []
        while self.ptr - 1 < self.size and self.arr[self.ptr - 1] is not None:
            rtn.append(self.arr[self.ptr - 1])
            self.ptr += 1
        return rtn


class Best_OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.id_val = {}
        for i in range(n):
            self.id_val[i + 1] = 0
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.id_val[idKey] = value
        if self.pointer == idKey:
            result = []
            while self.pointer < self.n + 1:

                value_re = self.id_val[self.pointer]
                result.append(value_re)
                # print(result)
                self.pointer += 1
                if self.pointer == self.n + 1:
                    return result
                if self.id_val[self.pointer] == 0:
                    return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
def test(cls, silent=True):
    input = [["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
             [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]]
    output = [[None, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]]
    for i in range(len(output)):
        s = cls(*input[2 * i + 1][0])
        result = [None]
        for j in range(1, len(input[2 * i])):
            result.append(eval("s.{0}(*{1})".format(input[2 * i][j], input[2 * i + 1][j])))
        if result != output[i]:
            if silent:
                raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(result) + ' !== ' + str(output[i]))
        if silent:
            print('Passed input: ' + str(input[i]))


test(OrderedStream)
# print(timeit.timeit(stmt=lambda: test(OrderedStream, False), number=1_000_000))
# print(timeit.timeit(stmt=lambda: test(Best_OrderedStream, False), number=1_000_000))
# Same time
# 28.747518666999895
# 28.359991042000274