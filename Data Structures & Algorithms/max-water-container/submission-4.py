class Solution:
    def maxArea(self, heights: List[int]) -> int:
        list1 = []
        lp = 0
        rp = len(heights) - 1
        area = 0
        while lp < rp :
            length = rp - lp
            height = min(heights[lp], heights[rp])
            x = length * height
            area = max(area, x)
            list1.append(x)
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1
        return area