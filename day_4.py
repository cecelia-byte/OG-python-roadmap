# functions
# def calc_Sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# calc_Sum(10,20)

# function to calculate average of 3 nos
# def calc_Avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg  

# calc_Avg(10,20,30)

# print the length of list
# marks=["delhi","mumbai","chennai","kolkata"]
# def length(list):
#     count=0
#     for i in list:
#         count+=1
#     print(count)
#     return count
# length(marks)
# def print_list(list):
#        for i in list:
#         print(i, end=" ")
        

# print_list(marks)     
# def factorial(n):
#     for i in range(1,n):
#         n=n*i
#     if n==0 or n==1:
#         print(1)
#         return 1
#     else:
#         print(n)
#         return n
# factorial(0)

# usd to inr
# def usd_to_inr(usd):
#     inr=usd*95
#     print(inr)

# usd_to_inr(100)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     print("hello")
#     show(n-1)

# show(5)
# # recursion factorial
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1) 
# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# print(sum(5)) 
list_1=[1,2,3,4,5]
def print_list(list, i):
    if (i==len(list)):
        return
    else: 
        print(list[i])
    print_list(list, i+1)
print_list(list_1,0)