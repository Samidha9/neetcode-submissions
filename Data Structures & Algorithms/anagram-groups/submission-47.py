class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       dict1 = defaultdict(list)
       for s in strs:
        count = [0] * 26
        for i in s:
            count[ord(i) - 97] += 1
        dict1[tuple(count)].append(s)
       return list(dict1.values())