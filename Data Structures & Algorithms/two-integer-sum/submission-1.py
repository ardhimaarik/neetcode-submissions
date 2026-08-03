class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}
        for idx, num in enumerate(nums): 
            diff = target - num
            if diff in seen_nums:
                return [seen_nums[diff], idx]
            seen_nums[num] = idx
        return []

        