class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        for i in s:
            if i.isalnum():
                list1.append(i.lower())
        print(list1)
        lp = 0
        rp = len(list1) - 1
        while lp < rp:
            if list1[lp] == list1[rp]:
                lp += 1
                rp -= 1
            else:
                return False
        return True










        '''list1=[]
        for i in s:
            if i.isalnum():
                list1.append(i.lower())
       
        lp=0
        rp=len(list1)-1
  
        while lp<rp:
            if list1[lp] != list1[rp]:
                return False
            else:
                lp +=1
                rp -=1
        return True'''