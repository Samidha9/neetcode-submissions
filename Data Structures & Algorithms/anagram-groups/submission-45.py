class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for val in strs:
            count = [0]*26
            for i in val:
                count[ord(i) - ord('a')] += 1
            dict1[tuple(count)].append(val)
        return list(dict1.values())