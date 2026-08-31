class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums = sorted(nums)
        # print(nums)

        for idx, num in enumerate(nums): 
            if idx > 0 and num == nums[idx-1]: 
                continue
            left, right = idx + 1, len(nums)-1
            while left < right: 
                total = num + nums[left] + nums[right]
                if total == 0: 
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                elif total < 0: 
                    left += 1
                else: 
                    right -= 1
        return result