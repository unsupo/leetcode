class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')

input=["1.1.1.1","255.100.50.0"]
output=["1[.]1[.]1[.]1","255[.]100[.]50[.]0"]
for i in range(len(input)):
    r = Solution().defangIPaddr(input[i])
    if r != output[i]:
        raise Exception('Failed: '+str(input[i])+' ---- Got: '+str(r)+' !== '+str(output[i]))
    print('Passed input: '+str(input[i]))