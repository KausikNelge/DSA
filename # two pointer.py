# two pointer 

# def reverse_array(arr):
#     left =0
#     right = len(arr) -1 


#     while    left < right :
#         temp = arr[left]
#         arr[left] = arr[right] 
#         arr[right] = temp
#         left += 1
#         right -= 1

#     return arr

# test_arr = [10, 20, 30, 40, 50]
# print((reverse_array)(test_arr))

# arr = [0, 1, 0, 3, 12]
# left = 0 

# for right in range (len(arr)):
#     temp = arr[left]
#     if right != 0 :
#         arr[left] = arr[right]
#         arr[right] = temp
#         left += 1





# print(arr)        
# arr = [5,5,8,0,8,6,8]
# def count_distinct(arr):
#     return len(set(arr))

# print(count_distinct(arr))

arr = [1,2,3,1]
def contains_dup(arr):
    seen = set()
    for  num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


print(contains_dup(arr))

  
        











