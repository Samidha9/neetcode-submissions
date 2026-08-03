class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1= dict()
        list1=[]
        list4=[]
        for i in nums:
            dict1[i] = 1 + dict1.get(i, 0)

        for key, value in dict1.items():
            list1.append([value,key])
        print(list1)
        list2=sorted(list1)
        print(list2)
        list3=list2[-k::]
        for i in list3:
            list4.append(i[1])
        print(list4)
        return list4