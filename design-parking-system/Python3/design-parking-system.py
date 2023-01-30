class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        r = self.lots[carType-1] > 0
        self.lots[carType-1] -= 1
        return r


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

input = [["ParkingSystem", "addCar", "addCar", "addCar", "addCar"], [[1, 1, 0], [1], [2], [3], [1]]]
output = [[None, True, True, False, False]]
for i in range(len(output)):
    s = ParkingSystem(*input[2 * i + 1][0])
    result = [None]
    for j in range(1, len(input[2 * i])):
        result.append(eval("s.{0}(*{1})".format(input[2 * i][j], input[2 * i + 1][j])))
    if result != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(result) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
