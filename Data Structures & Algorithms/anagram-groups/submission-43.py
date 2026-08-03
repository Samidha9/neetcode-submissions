class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char) - ord('a')] += 1
            dict1[tuple(count)].append(i)
        return list(dict1.values())