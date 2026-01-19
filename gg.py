class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left =0
        right = len(numbers)-1
        for i in range(len(numbers)):
            if numbers[i] + numbers[right] == target:
                i+=1
                right+=1
                return i,right
            else:
                while numbers[i] + numbers[right] == target:
                    right -=1
                
            i+=1
            right+=1
            return i,right















        # while numbers[left] < numbers[right]:
        #     if numbers[left] + numbers[right] == target:
        #         left+=1
        #         right+=1
        #         return left,right
        #     break
        # else:
