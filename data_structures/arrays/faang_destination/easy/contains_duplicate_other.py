"""
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


class Solution:
  def contains_duplicate_sliding_window(self, nums:list[int], k: int)->bool:
      if (k<=0):
         return False
      
      emptyHashSet: set[int] = set()
      
      for i,num in enumerate(nums):
          if(num in emptyHashSet):
             return True
          else:
             emptyHashSet.add(num)
             
          if(len(emptyHashSet) >k):
              emptyHashSet.remove(nums[i-k])
                
      return False
      


if __name__ == "__main__":
   s = Solution()
   print(s.contains_duplicate_sliding_window([1,0,1,1], 3))
        