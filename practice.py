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

n= 36
s = int(math.sqrt(n))
for i in range(1,s+1):
    if n % i  == 0:
        print(i)
        helper = n//i
        if helper != i:
            print(helper)