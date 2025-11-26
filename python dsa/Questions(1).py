## count digit
# class solution:
#     def countdigit(self,n):
#         count=0                       or                   return len(str(n))
#         while n >0:
#             count   = count+1 
#             n= n//10
#         return count
            
# s=solution()
# print(s.countDigit(224))


## reverse a number
# class solution:
#     def reverse(self,n):
#         return int(str(n)[::-1])
                                            
# s=solution()
# num=int(input("enter no:"))
# print(s.reverse(num))              


## palindrome
# def palindrome(n :str)-> bool:
#     return n==n[::-1]

# q=input("")
# print(palindrome(q))

#or

# def pal(n:int)->bool:
#     if n<0:
#         return False
#     orignal=n
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev * 10 + digit
#         n=n//10
        
#     return rev==orignal

# print(pal(565))    
        
        
        
        
## greatest common divisor(gcd)  ## eucliden

# a=12
# b=9

# while a and b >0:
#     if a>b:
#        a= a%b
#     else:
#         b=b%a
        
# if a == 0:
#     print(b)
# else:
#     print(a)            

## armstrong no

# n=153
# original=n
# sum=0
# while n > 0:
#     digit = n % 10
#     sum =sum + digit ** 3
#     n //= 10

    
# if sum==original:
#     print("True")
# else :
#     print("false")    
        
        
        
## print divisors

# a=36

# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
        

## prime
n=int(input("enter no:"))

if n<2:
    print("not prime")
    
    
for i in range(2,n):
    if n % i==0:
        print("not prime")
    else:
        print(" prime")        