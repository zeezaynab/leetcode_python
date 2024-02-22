class Solution(object):
    def singleNumber(self, nums):
        nums2=[]
        for i in nums:
            if nums.count(i)==1 and i not in nums2:
                return(i)
