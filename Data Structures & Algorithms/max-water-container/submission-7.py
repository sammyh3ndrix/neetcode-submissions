class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #ok were gonna use left and irght pointers to get the begiiigng and end indidex
        left = 0
        right = len(heights)-1
        size = 0
        #initilizaing varible named size so we can return it
        while left < right:
            #while left index is less than right becuase we are going from both ends inward
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            # area equal height times widith we got width by suctract right index from left and we got height but get tting the min value of the idk acutally lol
            size = max(area, size)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return size
        