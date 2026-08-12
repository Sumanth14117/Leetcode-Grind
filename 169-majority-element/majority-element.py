class Solution(object):
    def majorityElement(self, nums):
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        max=0
        ans=None
        for num in seen:
            if seen[num]>max:
                max=seen[num]
                ans=num
        return ans
        