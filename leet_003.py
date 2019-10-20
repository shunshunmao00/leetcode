class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        norep = {'r': 0, 'l': 0, 'q': 0, 'z': 0, 'c': 0, 'x': 0, 'y': 0, 'i': 0, 'n': 0, 'v': 0, 'u': 0, 'e': 0, 'g': 0, 'd': 0, 'f': 0, 'j': 0, 's': 0, 'w': 0, 'm': 0, 't': 0, 'p': 0, 'k': 0, 'b': 0, 'h': 0, 'o': 0, 'a': 0}

        re = 0
        count = 0
        for letter in s:
            if letter not in norep:
                norep[letter] = 0
            if count == 0 or norep[letter] == 0:
                count += 1
                norep[letter] = count
                re = max(re, count)
            else:
                part = norep[letter]
                for key in norep:
                    if norep[key] > part:
                        norep[key] -= part
                    else:
                        norep[key] = 0
                count -= part
                count += 1
                norep[letter] = count

        return re

    def reset(self):
        dirt = {'r': 0, 'l': 0, 'q': 0, 'z': 0, 'c': 0, 'x': 0, 'y': 0, 'i': 0, 'n': 0, 'v': 0, 'u': 0, 'e': 0, 'g': 0, 'd': 0, 'f': 0, 'j': 0, 's': 0, 'w': 0, 'm': 0, 't': 0, 'p': 0, 'k': 0, 'b': 0, 'h': 0, 'o': 0, 'a': 0}
        return dirt

if __name__ == "__main__":
    solution = Solution()
    text = 'abcabcbb'
    print( solution.lengthOfLongestSubstring(text))