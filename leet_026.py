class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        idx = []
        while i<len(nums):

            if nums[i] in idx:
                del(nums[i])
            else:
                idx.append( nums[i])
                i += 1
        return len(nums)
if __name__ == "__main__":
    solution = Solution()
    nums =  [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))
    print(nums)

'''
 解法-双指针

首先注意数组是有序的，那么重复的元素一定会相邻。

要求删除重复元素，实际上就是将不重复的元素移到数组的左侧。

考虑用 2 个指针，一个在前记作 p，一个在后记作 q，算法流程如下：

1.比较p 和 q 位置的元素是否相等。

如果相等，q 后移 1 位
如果不相等，将 q 位置的元素复制到 p+1 位置上，p 后移一位，q 后移 1 位
重复上述过程，直到 q 等于数组长度。

返回 p + 1，即为新数组长度。

'''