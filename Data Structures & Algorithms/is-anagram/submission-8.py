class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict1[t[i]] = dict1.get(t[i], 0) - 1
      
        for val in dict1.values():
            if val != 0:
                return False
        return True
       





























       

        ''' if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        print(dictS)
        print(dictT)
        return dictS == dictT'''