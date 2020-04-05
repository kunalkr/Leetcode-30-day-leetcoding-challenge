class Solution:

    def isHappy(self, n: int) -> bool:
        def getSquareSum(n):
            sum = 0
            while n:
                sum += (n%10)**2
                n = n//10
            return sum
        
        approach = 2

        if approach == 1:
            slow = fast = n

            while True:
                slow = getSquareSum(slow)
                fast = getSquareSum(getSquareSum(fast))

                if slow == fast:
                    break

            return slow == 1
        else:
            visited = set()
            while True:
                n = getSquareSum(n)

                if n in visited:
                    break
                visited.add(n)

            return n == 1
