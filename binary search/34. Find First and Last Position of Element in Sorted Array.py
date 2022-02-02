class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binary(nums,target,True)
        right=self.binary(nums,target,False)
        return [left,right]
        
    
    
    
    def binary(self,nums,t,biase):
        s,e=0,len(nums)-1
        i=-1
        while (s<=e):
            m= s+(e-s)//2
            if t < nums[m]:
                e=m-1
            elif t> nums[m]:
                s=m+1
            else:
                i=m
                if (biase):
                    e=m-1
                else:
                    s=m+1
        return i
        