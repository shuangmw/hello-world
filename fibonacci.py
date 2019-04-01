# Fibonacci
# Solution 1: Recursion
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2)
# Solution 2: loop
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            t1, t2 = 1, 2
            i = 3
            while(i<=number):
                total = t1+t2
                t1 = t2
                t2 = total
                i += 1
            return total
