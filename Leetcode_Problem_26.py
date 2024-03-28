# sol 1

def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    nums[:]=sorted(set(nums))
    return len(nums)

# sol 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nnums = []
        for i in nums:
            if not i in nnums:
                nnums.append(i)
        nums[:]=sorted(nnums)
        return len(nums)
