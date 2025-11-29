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

# def print_1_to_n(n):
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
