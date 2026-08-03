class Solution:
    def encode(self, strs: List[str]) -> str:
        '''s=''
        if not strs:
            return str(strs)
        for i in strs:
            if not s:
                s = i
            else:
                s=s+"_"+i
        return s'''
        s = ''
        for i in strs:
            n = len(i)
            if not s:
                s = i + "cv67" + str(n)
            else:
                s = s + "cv67" + i  + "cv67" + str(n)
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        list2 = s.split("cv67")
        print(list2)
        list3= []
        for i in range(0,len(list2)-1,2):
            list3.append(list2[i])
        return list3
        

        '''print(s)
        if s == "[]":
            return []
        return s.split("_")'''
