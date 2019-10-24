'''
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s) - 1
        idx = 0
        num = 0
        while idx < length:

            if s[idx] == 'M':
                num += 1000
                idx += 1

            elif s[idx] == 'D':
                num += 500
                idx += 1

            elif s[idx] == 'C':
                if s[idx+1] == 'D':
                    num += 400
                    idx += 2
                elif s[idx+1] == 'M':
                    num += 900
                    idx += 2
                else:
                    num += 100
                    idx += 1

            elif s[idx] == 'L':
                num += 50
                idx += 1

            elif s[idx] == 'X':
                if s[idx+1] == 'L':
                    num += 40
                    idx += 2
                elif s[idx+1] == 'C':
                    num += 90
                    idx += 2
                else:
                    num += 10
                    idx += 1

            elif s[idx] == 'V':
                num += 5
                idx += 1

            elif s[idx] == 'I':
                if s[idx+1] == 'X':
                    num += 9
                    idx += 2
                elif s[idx+1] == 'V':
                    num += 4
                    idx += 2
                else:
                    num += 1
                    idx += 1
        if idx == len(s)-1:
            if s[idx] == 'M':
                num += 1000
            elif s[idx] == 'D':
                num += 500
            elif s[idx] == 'C':
                num += 100
            elif s[idx] == 'L':
                num += 50
            elif s[idx] == 'X':
                num += 10
            elif s[idx] == 'V':
                num += 5
            elif s[idx] == 'I':
                num += 1

        return num



if __name__ == "__main__":
    solution = Solution()
    text = "MMMXLV"

    print(solution.romanToInt(text))