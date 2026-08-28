class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        uniq = set(nums)
        max_seq = 0

        for idx, num in enumerate(nums): 
            startseq = num-1
            if startseq not in uniq: 
                nextseq = num+1
                curr_length = 1
                while nextseq in uniq:
                    curr_length += 1
                    nextseq += 1
                    
                max_seq = max(max_seq, curr_length)
        return max_seq
        # nums = list(set(nums))
        # # print(nums)
        # data = [0] * (max(nums)-min(nums)+1)
        # # print(data)
        # exist = set()
        # minnums = min(nums)
        # for x in nums: 
        #     exist.add(x)
        #     data[x-minnums] = 1
        # # print(data)
        # max_lenght = 0
        # curr_lenght = 0
        # for idx, num in enumerate(data): 
        #     if num == 0: 
        #         max_lenght = max(max_lenght, curr_lenght)
        #         curr_lenght = 0
        #     else: 
        #         curr_lenght += 1
        # if curr_lenght != 0: 
        #     max_lenght = max(max_lenght, curr_lenght)
        #     curr_lenght = 0
        # return max_lenght