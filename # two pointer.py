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

arr = [0, 1, 0, 3, 12]
left = 0 

for right in range (len(arr)):
    temp = arr[left]
    if right != 0 :
        arr[left] = arr[right]
        arr[right] = temp
        left += 1





print(arr)        














