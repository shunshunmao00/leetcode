'''
20. 有效的括号
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                stack.append(item)
            elif len(stack) == 0:
                return False
            elif item == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else :
                    return False
            elif item == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else :
                    return False
            elif item == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    text = '(]'
    print( solution.isValid(text))