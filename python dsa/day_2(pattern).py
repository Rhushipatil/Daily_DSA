##1


for i in range(1,6):
    for j in range(1,6):
        print("*", end="" )

    print()    

##2
# n=int(input("enter no :"))    

# for i in range(1,n+1):
#     for j in range(i):
#         print("*" ,end="")
#     print()    
   
##3 

# for i in range(2,6):
   
#     for j in range(1,i+1):
#         print(j, end="")
#     print()    

##4

# for i in range(1,6):
#     for j in range(i):
#         print(i, end="")
#     print()    

## 5

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j , end="")
#     print()    


##6
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*" , end="")
#     print()    

## 7
# n=5
# for i in range(1,n+1):
#     space="   " *(n-i)
#     star= " * " *(2* i-1)
#     print(space + star)


## 8

# n=5
# for i in range(n,0,-1):
#     space=" " *(n-i)
#     star="*" *(2*i -1)
#     print(space + star)
    

##9

# n=5
# for i in range(1, n+1):
#     space=" " * (n-i)
#     star="*" * (2*i-1)
#     print(space + star)    
    
# for j in range(n-1,0,-1):
#     space=" " * (n-j)
#     star="*" * (2*j-1)
#     print(space + star)    
    
    #10
    
# n=5

# for i in range(1,n+1):
#     print("*" * i)    
# for j in range(n,0,-1):
#     print("*" * j)     


## 11

# n=5
# for i in range(1,n+1):
#     val=i  %2
#     for _ in range(i):
#         print(val, end="")
#         val= 1- val
#     print()    
