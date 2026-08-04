class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n , 0) + 1
        arr = []
        for key, val in count.items():
            arr.append([val, key])
        arr.sort()
        res = []
        while (len(res))< k:
            res.append(arr.pop()[1])
        return res
            
        




























    


    ''' dict1 = {}
        for num in nums:
            dict1[num] = 1 + dict1.get(num, 0)
        heap = []
        for num in dict1:
           heapq.heappush(heap, (dict1[num] , num)) 
           if len(heap) > k:
                heapq.heappop(heap)
        list1 = []
        for i in range(k):
            list1.append(heapq.heappop(heap)[1])
        return list1'''






















    '''dict1= dict()
        list1=[]
        list4=[]
        for i in nums:
            dict1[i] = 1 + dict1.get(i, 0)

        for key, value in dict1.items():
            list1.append([value,key])
        
        list2=sorted(list1)
        
        print(list2)
        list3=list2[-k::]
        for i in list3:
            list4.append(i[1])
        print(list4)
        return list4'''