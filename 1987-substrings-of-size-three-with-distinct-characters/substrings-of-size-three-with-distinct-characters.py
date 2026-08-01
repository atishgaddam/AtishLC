class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        temp = ""
        l = 0
        for r in range(n):
            temp = temp+s[r]
            if(r-l==3):
                temp = temp[1:]
                l = l+1
            if(r-l+1 == 3 and len(set(temp))==3):
                ans+=1
        return ans
