class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        list1 = []
        while lp < rp:
            add = numbers[lp] + numbers[rp]
            if add == target:
                list1.append(lp+1)
                list1.append(rp+1)
                return list1
            elif add > target:
                rp -= 1
            else:
                lp += 1
                
        print(list1)
           