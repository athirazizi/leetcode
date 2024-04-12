class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
    
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'