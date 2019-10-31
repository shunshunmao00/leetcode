from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        idx = 1
        ans = nums[0]
        if len(nums) > 1:
            while idx<len(nums):
                # print(ans)
                if count == 0:
                    ans = nums[idx]
                    count = 1
                    idx += 1
                    continue
                if nums[idx] == ans:
                    count += 1
                else:
                    count -= 1
                idx += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print( solution.majorityElement([3,2,3]))


'''
[10,9,9,9,10]
[2,2,1,1,1,2,2]
[3,2,3]
'''
'''

方法 6：Boyer-Moore 投票算法

想法

如果我们把众数记为 +1+1+1 ，把其他数记为 −1-1−1 ，将它们全部加起来，显然和大于 0 ，从结果本身我们可以看出众数比其他数多。

算法

本质上， Boyer-Moore 算法就是找 nums 的一个后缀 sufsufsuf ，其中 suf[0]suf[0]suf[0] 就是后缀中的众数。我们维护一个计数器，如果遇到一个我们目前的候选众数，就将计数器加一，否则减一。只要计数器等于 0 ，我们就将 nums 中之前访问的数字全部 忘记 ，并把下一个数字当做候选的众数。直观上这个算法不是特别明显为何是对的，我们先看下面这个例子（竖线用来划分每次计数器归零的情况）

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]

首先，下标为 0 的 7 被当做众数的第一个候选。在下标为 5 处，计数器会变回0 。所以下标为 6 的 5 是下一个众数的候选者。由于这个例子中 7 是真正的众数，所以通过忽略掉前面的数字，我们忽略掉了同样多数目的众数和非众数。因此， 7 仍然是剩下数字中的众数。

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

现在，众数是 5 （在计数器归零的时候我们把候选从 7 变成了 5）。此时，我们的候选者并不是真正的众数，但是我们在 遗忘 前面的数字的时候，要去掉相同数目的众数和非众数（如果遗忘更多的非众数，会导致计数器变成负数）。

因此，上面的过程说明了我们可以放心地遗忘前面的数字，并继续求解剩下数字中的众数。最后，总有一个后缀满足计数器是大于 0 的，此时这个后缀的众数就是整个数组的众数。

class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}

复杂度分析

    时间复杂度：O(n)O(n)O(n)

    Boyer-Moore 算法严格执行了 nnn 次循环，所以时间复杂度是线性时间的。

    空间复杂度：O(1)O(1)O(1)

    Boyer-Moore 只需要常数级别的额外空间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/majority-element/solution/qiu-zhong-shu-by-leetcode-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''