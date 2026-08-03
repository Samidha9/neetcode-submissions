class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            



    '''s = ''
        for i in strs:
            if not s:
                s = i + "cv67" + "_"
                
            else:
                s = s + "cv67" + i  + "cv67" + "_"   
        return s


    def decode(self, s: str) -> List[str]:
        list2 = s.split("cv67")
        list3= []
        for i in range(0,len(list2)-1,2):
            list3.append(list2[i])
        return list3'''