class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # O(N*M) times and O(M+N) space
        if '0' in [num1, num2]:
            return '0'

        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                if res[i1 + i2] >= 10:
                    res[i1 + i2 + 1] += res[i1 + i2]//10
                    res[i1 + i2] = res[i1 + i2] % 10
        res = res[::-1]
        ptr = 0

        while ptr < len(res) and res[ptr] == 0:
            ptr += 1
        res = res[ptr:]
        for i in range(len(res)):
            res[i] = str(res[i])
        ans = ''.join(res)
        return ans 