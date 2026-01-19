# #2 sq = int(input("enter square "))
# # square = sq**2
# # print(square)

# # 3
# a =10
# b =20
# sum  = a+b 
# diff = a-b
# prod = a*b
# div = a/b

# 4
# n = 9
# if n % 10 == 0:
#     print("even")

# else: print("odd")

# # 5
# n=-1
# if n >=0:
#     print("positive")
# elif n == 0:
#     print("0")
# else:
#     print("-ve")

# 6
# c= 22
# f = c * 9/5 +32
# print(f)

# 7
# its very easy 


# # 8
# n = [2,4,6]
# n.sort()
# lar = n[-1]
# print(lar)


# 9

# n = [2,3]

# n.remove(2)
# n.append(2)
# print(n)

# /10
# n =10 
# for i in range(1,n+1):
#     print(i)


# /11
# def even_num():
# n =15
     
# for i in range (1, n+1):
#     if i %2 == 0:
#         print(i)

# # 12
# n =15
# for i in range (0, n):
#     i+=1
#     print(i)
 
#  13

# n =2
# print(n)
# for i in range (n,11):
    
#      nb= n*i
#      print(nb)
# 14  
# n  = 1234
# b = len(str(n))
# print(b)

# 15
# n =1234
# rev_num = 0
# while n> 0:
#     last_digit = n %10
#     rev_num = rev_num *10 + last_digit
#     n= n//10
# print(rev_num)
# i have copied logic of it


# /16
# n = 121
# on =n 
# rev_num = 0
# while n> 0:
#     ld = n% 10
#     rev_num = rev_num *10 + ld
#     n= n//10

# if rev_num == on:
#     print("palindrome")
# else:
#     print("not")


# 17 is prime

# n =14
# while n> 0:
#     if n == 2:
#         print("prime") 
#         break
    
#     if n %2 == 0 :
#         print('not a primne')
#         break

#     else:
#          print("prime")
# #          break
# # 18
# n =18

# count = 0

# for i in range (1,n+1):
#     if n % i == 0:
#         count +=1
#     # print(n)
#     count = count*10 + n
# helper = n //10
# print(n)






# 18
# n =12
# for num in range (2,n+1):
#     prime = True
#     for i in range(2,num):
#         if n % 2 == 0:
#               prime = False
#               break
# if prime:
#     print(num)



# /19
# n =5 
# fact =1
# for i in  range (1,n+1):
#     fact *= i


# print(fact)
# n =5
# fact  =1 
# for i in range(1,n+1):
#     fact *= i

# print(fact)
# n=8
# prev = 0
# curr =1
# print(prev)
# print(curr)
# for i in range (n-1):
#     prev,curr = curr, prev+ curr
#     print(curr)


# 21
# strn = "fsfsefsffhjols" 
# vo = "a","e","i","o","u"
# count = 0
# for sh in strn:
#     if sh in vo:
#         count+=1
# print(count)
# vo = "a","e","i","o","u"
# for st in strn:
#     if st in vo:
#         count+=1
#     print(count)


# strn = "fdsjhf"
# list1 = list(strn)

# n = list1[:: -1]
       
# n1 = "".join(n)
# print(n1)

# str111 = "fsdjfsd"
# arr = list(str111)
# n = arr[:: -1]
# n1 = "".join(n)
# print(n1)


# str11 = "Gadag"
# b= str11.lower()

# on = b
# arr = list(b)
# n = arr[:: -1]
# n1 = "".join(n)
# if n1 == on:
#     print("plaindrome")



# str1 = "gadag"
# arr = list(str1)
# left =0 
# right = len(arr)-1
# while left <right:
#     if arr[right] != arr[left]:
#         break
#     else:
#         left +=1
#         right -=1

# 
# str1 ='anaram'
# b = {}
# # print(b)
# for char in str1:
#     if char in b:
#         b[char]

# print(b)

# arr=[2,4,6]
# mul=[]

# for num in arr:
#     mul.append(num**2)

# print(mul)


arr =[2,3,9]
sq = []
for num in arr:
    sq.append(num**2)

print(sq)
































