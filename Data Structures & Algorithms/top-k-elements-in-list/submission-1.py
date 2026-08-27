class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: 
            if num in freq: 
                freq[num] = freq[num] + 1
            else : 
                freq[num] = 1
        
        prio = [[] for _ in range(len(nums)+1)]
        for n, c in freq.items(): 
            prio[c].append(n)
        
        result = []
        for val in range( len(prio)-1, 0, -1): 
            for i in prio[val]: 
                result.append(i)
                if len(result) == k: 
                    return result
        return result