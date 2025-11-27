##nprint n times Recursion

# def hello():
#     hello()

def prt_name(name,n):
    if n==0:
        return
    print(name)
    prt_name(name ,n-1)
    
prt_name("rhushi", 3)    