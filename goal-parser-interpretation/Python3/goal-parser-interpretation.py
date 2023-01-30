class Solution:
    def interpret(self, command: str) -> str:
        # ()=o and (al)=al
        return command.replace("()", "o").replace("(al)", "al")


input = ["G()(al)", "G()()()()(al)", "(al)G(al)()()G"]
output = ["Goal", "Gooooal", "alGalooG"]
for i in range(len(output)):
    r = Solution().interpret(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
