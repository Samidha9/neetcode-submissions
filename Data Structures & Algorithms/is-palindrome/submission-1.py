class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=[]
        for i in s:
            if i.isalnum():
                string.append(i.lower())
        print(string)
        lp=0
        rp=len(string)-1
        print(rp)
        while lp<rp:
            if string[lp] != string[rp]:
                return False
            else:
                lp +=1
                rp -=1
        return True