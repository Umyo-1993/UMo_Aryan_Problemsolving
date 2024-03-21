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
