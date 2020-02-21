from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idxf = 0
        idxb = 0
        end = len(nums)
        while idxf < end and nums[idxf] != 0:
            idxf += 1
            idxb += 1
        while idxf < end:
            if nums[idxf] == 0:
                idxf += 1
            else:
                nums[idxb] = nums[idxf]
                idxf += 1
                idxb += 1

        while idxb < end:
            nums[idxb] = 0
            idxb += 1

        print(nums)

if __name__ == "__main__":
    solution = Solution()
    t = [0, 1, 0, 3, 12]
    solution.moveZeroes(t)