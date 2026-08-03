class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for s in st:
                count[ord(s) - ord('a')] += 1
            dict1[tuple(count)].append(st)
        return list(dict1.values())
