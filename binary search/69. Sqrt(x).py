class Solution:
    def mySqrt(self, x: int) -> int:
        if X==0 or x==1:
            return x
        
        s=0
        e=x
        while s<=e:
            mid= s+(e-s)//2
            
            if mid*mid == x:
                return mid
            
            elif mid* mid <x:
                s=mid+1
                ans=mid
            else:
                e=mid-1
        return ans