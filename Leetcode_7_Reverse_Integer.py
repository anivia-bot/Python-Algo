class Solution:
    def reverse(self, x: int) -> int:

        # O(n) time and O(1) space
        maxNum = 2147483647
        minNum = -2147483648

        res = 0

        while x:
            digit = int(math.fmod(x,10))
            x = int(x / 10)

            if (res > maxNum // 10 or (res == maxNum // 10 and digit >= maxNum % 10)):
                return 0
            if (res < minNum // 10 or (res == minNum // 10 and digit <= minNum % 10)):
                return 0


            res = (res*10) + digit
        return res