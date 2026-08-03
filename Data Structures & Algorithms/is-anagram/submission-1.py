class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS= dict()
        dictT= dict()
        if len(s) != len(t):
            return False
        else:
            for char in s:
                if char in dictS:
                    dictS[char]+=1
                else:
                    dictS[char]=1
            print(dictS)
            for char in t:
                if char in dictT:
                    dictT[char]+=1
                else:
                    dictT[char]=1
            print(dictT)
        if dictS==dictT:
            return True
        else:
            return False