
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dinums={}
        leng=len(nums)
        for i in range(leng):
            val=target-nums[i]
            if val in dinums:
                return [dinums[val],i]
            dinums[nums[i]]=i      
#------------------------------------
from typing import List
example1=[1,4,12,9,6,4,3,8]

def twoSum( nums: List[int], target: int) -> List[int]:
        leng=len(nums)
        for i in range(leng):
            val=target-nums[i]
            if val in nums:
                return [nums.index(val),i]
            
x=twoSum(example1,8)
print(x)
#----------------------------------      

