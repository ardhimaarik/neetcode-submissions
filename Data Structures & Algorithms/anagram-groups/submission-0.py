import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: 
            return [strs]
        dictionary = collections.defaultdict(list)
        
        for left, item in enumerate(strs): 
            # key = tuple(sorted(item))
            # dictionary[key].append(item)

            count = [0]*26
            for s in item: 
                count[ord(s) - ord('a')] += 1
                #print(ord(s), ord('a'))
                #print(count[ord(s) - ord('a')])
            dictionary[tuple(count)].append(item)
        return list(dictionary.values())