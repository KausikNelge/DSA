# # n = 450
# # count = 0
# # while n > 0:
# #      n= n // 10
# #      count += 1

# # # print(count)
# n= 7789
# reverse_num = 0
# while n > 0:
#     last_digit= n % 10
#     # print(last_digit)
#     reverse_num = (reverse_num * 10) + last_digit
#     n= n//10
    
# #     print(last_digit)

# # reverse_num = reverse_num *10  + last_digit
# print(reverse_num)

# n= 7899
# reverse_num = 0
# while n> 0:
#     last_digit = n % 10
#     reverse_num = reverse_num*10 + last_digit
#     n= n//10
# print(reverse_num)









# n= 455
# rev = 0 
# while n> 0:
#     ld= n % 10
#     rev = rev* 10 + ld
#     n = n//10

# print(rev)

# n =5666
# count=0 
# while n> 0:
#     n= n // 10
#     count+=1

# print(count)

# n= 121
# on = n
# rev =0 
# while n> 0:
#     ld= n%10
#     rev = rev*10 + ld
#     n= n//10
# print(rev)
# if rev == on:
#         print("True")
# else:
#         print("False")


# n = 1634
# on = n
# sum = 0 
# digits = len(str(n))
# while n> 0 :
#     ld = n % 10
#     sum= sum  + ld**digits
#     n= n//10

# if sum == on:
#     print("num in am") 




# n= 163
# on = n 
# sum = 0 
# digits = len(str(n))
# while n> 0:
#     ls = n % 10
#     sum = sum + ls ** digits
#     n= n//10

# if on == sum:
#     print("n in arm")

# else:
#     print("Falaw")


# n= 36

# for i in range (1, n+1):
#     if n % i == 0:
#         print(i)




# n = 50

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)
import math 

# n= 36
# s = int(math.sqrt(n))
# for i in range(1,s+1):
#     if n % i  == 0:
#         print(i)
#         helper = n//i
#         if helper != i:
#             print(helper)
# 16/01/26 /prime numebrs
# n =2
# count =0 

# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
#         # helper = n//i
#         # print(helper)
# #         if helper != i:
# #             count+=1
# # print(count)
# if count == 2:
#     print("prime")
# else:
#     print("not a prime")     

# n=10
# m=40

# for i in range(min(n,m),n+m+1):
#     if n% i == 0 and m%i == 0:
#         print(1,i)
#         break


# n=52
# m=10
# while n> 0 :
#     if n > m:
#         n= n%m
#     else:
#         m = m % n

# # print(a,b)

# if n==0:
#     print("gcd is", m)
# else:
#     print("gcd is", n)
# # shortcut


# # a = 52 b=10
# def gcd(a,b):
#     while b:
#         a,b = b, a%b    #here first a = 52 and b= 10 the operationn starts from the right a%b which is 52
#         print(a)                 #52/10 reminder 2  which gets stored in b and the b value is 10 which gets stored in a
#                          # now a =10 and b = 2  10/2 gives reminder 0 which  makes the condition  false whic is b = False
#                          # print(a)
# print(gcd(52,10))        



# n =5
# for i in range(0,n):
#     n= i+n
# print(n)

# def reverse_arr(arr):
#     arr = [1, 2, 3, 4, 5, 6]

#     left =0 
#     right= len(arr)-1
#     while left < right:
#         arr[left],arr[right] = arr[right],arr[left]
#         left += 1
#         right -=1


     
#     return[arr]
# print(reverse_arr([]))



# pcr = [3,5,6]
# b = pcr[ :: -1]

# print(b)









# arr = [3,4,3,2,6]
# seen = {}

# for num in seen:
#     if :
        



# 17/01/26

# fibonacci numbers
# 
# def fib_num(n):
#     if n< 0:
#         return " niGga"
#     elif n==1:
#         return [1]
#     elif n==2:
#         return [0,1]
#     else:
#         fib_seq = [0,1]
#         for i in range(2,n+1):
#             fib1= fib_seq [i-1] + fib_seq [i-2]
#             fib_seq.append(fib1)
#             return fib_seq
        
# print(fib_num(4))
# n= 5
# prev= 0
# curr = 1
# print(prev)
# print(curr)
# for i in range(n-2):
#     prev , curr = curr ,prev+curr
#     # curr+=1
#     print(curr)

# n =3
# prev =0
# curr = 1
# print(prev)
# print(curr)
# for i in range(n-1):
#     prev,curr = curr ,curr+prev
#     print(curr)


# n =8

# fibs = [0,1]
# prev = 0 
# curr = 1
# for i in range (n-2):
    
#     prev ,curr = curr,prev+curr
#     fibs.append(curr)
# print(fibs)

# nums = [1, 2, 3]
# seen = {}
# count = 0 
# for n in nums:
#     if n in seen:
#         print("not distinct")
#         break
#     seen[n]=True
# else:
#     print("distinct")


nums = [1, 2, 3]
seen = set()
for n in nums:
    if n in seen:
        seen[n]= True
        seen.add(n)
        print("True")
        break
else:
    print("false    ")







