##nprint n times Recursion

# def hello():
#     hello()

def prt_name(name,n):
    if n==0:
        return
    print(name)
    prt_name(name ,n-1)
    

prt_name("rhushi", 3)    

#Print 1 to N using Recursion



# def prt(n,num=1):
#     if num>n:
#         return
#     print(num)
#     prt(n,num+1)
    
# prt(5)    
    
#or

## def print_1_to_n(n):
#     if n==0:     # base condition
#         return
#     print_1_to_n(n-1) 
#     print(n)
    

# print_1_to_n(5)




#Print N to 1 using Recursion
# def prt(n):
    
#     if n<1:   # or n==0    | n==0 if and only is negative value is not prosent | but n<1 is always ok
#         return
#     print(n , end=" ")
#     prt(n-1)
        
# prt(-5)



#-----------------------------4/12/2025----------------------------------

## Sum of first N Natural Numbers

# def sum_n(n):
#     if n == 1:      # Base condition
#         return 1
#     return n + sum_n(n - 1)  # Recursive call

# # Example
# print(sum_n(5))  



## Factorial of a Number : Iterative and Recursive

# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial_iterative(5))   

# def factorial_recursive(n):
#     if n == 1 or n == 0:       # Base condition
#         return 1
#     return n * factorial_recursive(n - 1)

# print(factorial_recursive(5))   


## array reverse
# def reverse_recursive(arr, left, right):
#     if left >= right:   # base condition
#         return arr

#     arr[left], arr[right] = arr[right], arr[left]  

#     return reverse_recursive(arr, left + 1, right - 1)

# print(reverse_recursive([1, 2, 3, 4, 5], 0, 4))


#  ## easy
# arr = [1, 2, 3, 4, 5]
# print(arr[::-1])



#Check if the given String is Palindrome or not
# def is_palindrome(s, left, right):
#     # Base condition: If pointers cross, it's a palindrome
#     if left >= right:
#         return True

#     # If characters don't match → not a palindrome
#     if s[left] != s[right]:
#         return False

#     # Recursive call
#     return is_palindrome(s, left + 1, right - 1)

# s = "madam"
# print(is_palindrome(s, 0, len(s) - 1))


##fibonacci
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(8))



#     if n==0:     # base condition
#         return
#     print_1_to_n(n-1) 
#     print(n)
    

# print_1_to_n(5)




#Print N to 1 using Recursion
def prt(n):
    
    if n<1:
        return
    print(n , end=" ")
    prt(n-1)
        
prt(6)

