class Solution:
    def getSecondLargest(self, arr):
        x=sorted(set(arr))
        if len(x)<2:
            return -1
        return x[-2]
