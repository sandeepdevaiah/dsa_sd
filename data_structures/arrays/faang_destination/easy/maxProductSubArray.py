"""
https://leetcode.com/problems/maximum-product-subarray/description/

Maximum Product Subarray  
Medium  
Topics: Array, Dynamic Programming  
Companies: Amazon, Microsoft, Google, Adobe  

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.  

The test cases are generated so that the answer will fit in a 32-bit integer.  

You must write an algorithm that runs in O(n) time.  

Example 1:  
Input: nums = [2,3,-2,4]  
Output: 6  
Explanation: [2,3] has the largest product 6.  

Example 2:  
Input: nums = [-2,0,-1]  
Output: 0  
Explanation: The result cannot be 2, because [-2,-1] is not a contiguous subarray.  

Constraints:  
1 <= nums.length <= 2 * 10^4  
-10 <= nums[i] <= 10  
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.  

"""

class Solution:
  def max_product_sub_array(self, nums:list[int])-> int:
    #define a max and min pointer.. 2 pointer problem with DP
    min_value = nums[0]
    max_value = nums[0]
    result = max_value

    for i in range(1,len(nums)):
        curr = nums[i]
        temp_max = max (curr, max_value*curr,min_value*curr)
        min_value = min (curr, min_value*curr,max_value*curr)
        max_value = temp_max
        result = max(result,max_value)

    return result


if __name__ == "__main__":
    s = Solution()
    print(s.max_product_sub_array([2,3,-2,4]))
    #print(s.max_product_sub_array([2,3,-2,4]))
    
        


