"""
https://leetcode.com/problems/product-of-array-except-self/description/

Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""


class Solution:
   def product_of_array(self, nums: list[int])-> list[int]:
      prefix = 1
      postfix = 1
      result = [1] *len(nums)


      #solution multiply the prefix and then multiply the postfix value with the resultset
      #first get prefix array and then postfix array. In prefix. Take the element and multiply it with the product and we know the previous product

      for i in range(len(nums)):
        result[i] = prefix
        prefix = nums[i]* prefix
      
      for i in range(len(nums)-1,-1,-1):
         result [i] = result[i]* postfix
         postfix = postfix *nums[i]

      print(result)


if __name__ == "__main__":
   s = Solution()
   s.product_of_array([1,2,3,4])
        