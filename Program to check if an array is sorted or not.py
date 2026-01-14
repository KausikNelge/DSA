
# Program to check if an array is sorted or not

class Solution:
    def isSorted(self, arr) -> bool:
        # code heref 
        for i in  range(len(arr -1)):
            if arr[i] > arr[i+1]:
                return False
                
        else:
            return True
            