 #Longest Substring Without Repeating Characters
 #Umo's Code
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        val=set()
        res=0

        for r in range(len(s)):
            while s[r] in val:
                val.remove(s[l])
                l+=1
            val.add(s[r])
            res=max(res,r-l+1)

        return res
  #Aryan's Code

# a ryan codᵉ

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, sli, sll = len(s), None, None
        sl = min(1,l)
        for i in range(l):
            for j in range(l-i+1):
                j+=i+1
                sli = s[i:j]
                sll = len(sli)
                if sll==len(set(sli)):
                    sl = max(sll,sl)
                else:
                    break
        return sl
