class Solution:

    def isHappy(self, n: int) -> bool:
        def getSquareSum(n):
            sum = 0
            while n:
                sum += (n%10)**2
                n = n//10
            return sum

        slow = fast = n

        while True:
            slow = getSquareSum(slow)
            fast = getSquareSum(getSquareSum(fast))
            
            if slow == fast:
                break
        
        return slow == 1
