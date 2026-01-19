class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left =0
        right = len(numbers)-1
        for i in range(len(numbers)):
            if numbers[i] + numbers[right] == target:
                i+=1
                right+=1
                return i,right

            elif numbers[i] + numbers[right] != target:
                
                  while numbers[i] + numbers[i+1] != target:
                right -=1
                # i+=1
                break
            i+=1
            right-=1
            return i,right
            
        else:
            if numbers[i] + numbers[right] != target:
                # i +=2
                # right+=2
                # break
        return i,right
                
            
            
                

            














        # while numbers[left] < numbers[right]:
        #     if numbers[left] + numbers[right] == target:
        #         left+=1
        #         right+=1
        #         return left,right
        #     break
        # else:
