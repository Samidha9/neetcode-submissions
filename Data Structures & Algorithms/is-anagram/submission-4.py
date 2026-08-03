class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Since the words will only be lower case

        if len(s) != len(t):
            return False
        else:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
                count[ord(t[i]) - ord('a')] -= 1
            for i in count:
                if i != 0:
                    return False
            return True