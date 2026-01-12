# arr = [16, 17, 4, 3, 5, 2]


# for i in range(0,len(arr)) :
#     if  < i:
#         leader= i

# print(leader)
arr = [16, 17, 4]

# for i, num in enumerate(arr):
#     print(f"Index: {i}, Value: {num}")


# arr = [16, 17, 4, 3, 5, 2]
# leader=[]
# n= len(arr)

# for i in range(n):
#     is_leader= True

#     for j in range(i+1,n):
#         if arr[j] > arr[i]:
#             is_leader= False
#             break

#         if is_leader:
#             leader.append(arr[i])

# print(leader)            
arr = [16, 17, 4, 3, 5, 2]
leaders=[]
max = -1


for i in range(len(arr)-1,-1,-1):
    current_num = arr[i]
    if arr[i] >= max:
        leaders.append(current_num)
        max = current_num


print(leaders[:: -1])
