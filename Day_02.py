#Move All Zeroes to End

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
        n = len(arr)
        j = 0
        for i in range(n):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        return arr
