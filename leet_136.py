from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        if len(nums) > 1:
            idx = 1
            while idx < len(nums):
                ans = ans ^ nums[idx]
                idx += 1
        return ans

        pass
if __name__ =="__main__":
    solution = Solution()
    print(solution.singleNumber( [4,1,2,1,2] ) )

'''
大脑的思考过程

这题拿到手，第一反应是用hash表，没有思考细节，只是觉得hash表肯定是可以搞定的，但是空间复杂度是 O(n)O(n)O(n)，不满足题意。

接着开始思考，如何才能做到空间复杂度是 O(1)O(1)O(1) 呢？脑袋开始疯狂打转，但没有思路。没办法，退回原点。

心想，如果使用暴力破解法，该如何解决，很简单：每次从数组中取一个数，记为cur，然后从剩下的数中查找，如果找不到，则cur即为要找的那个数。这种解法时间复杂度是 O(n2)O(n^2)O(n2)。

继续思考，如何再继续降低复杂度呢？ 想到了排序 ！！！

再继续思考，如何能把时间复杂度降到 O(n)O(n)O(n)，有两个突破点：

    暴力解法做了很多重复的工作
    要充分利用题目的已有信息

通过第一点，我没有想到思路，不知道有没有 DP 的解法，可能本人对DP使用不是太熟。
通过第二点，我还真找到突破口。反复看了好几篇题目，找到了一个很重要的信息：除了某个元素只出现一次以外，其余每个元素均出现两次。 觉得这是个突破口！！！！——异或运算！
解法一：暴力查找

两次循环，代码略
解法二：排序

使用快排，复杂度 O(nlogn)O(nlogn)O(nlogn)
解法三：

利用 Hash 表，Time: O(n)O(n)O(n) Space: O(n)O(n)O(n)

class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer i : nums) {
            Integer count = map.get(i);
            count = count == null ? 1 : ++count;
            map.put(i, count);
        }
        for (Integer i : map.keySet()) {
            Integer count = map.get(i);
            if (count == 1) {
                return i;
            }
        }
        return -1; // can't find it.
    }
}

解法四：异或

int ans = nums[0];
if (nums.length > 1) {
   for (int i = 1; i < nums.length; i++) {
      ans = ans ^ nums[i];
   }
 }
 return ans;

作者：yinyinnie
链接：https://leetcode-cn.com/problems/single-number/solution/xue-suan-fa-jie-guo-xiang-dui-yu-guo-cheng-bu-na-y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''