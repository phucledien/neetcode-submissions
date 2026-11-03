class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if seen.get(i):
                return True
            seen[i] = True
        return False
        