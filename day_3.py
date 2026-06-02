# # sets
# collection={1,2,3,2,2,"hello","world"}
# # print(collection)
# # print(type(collection))
# print(len(collection))
# empty set
# my_set=set()
# my_set.add(1)
# my_set.add(2)
# my_set.add(2)
# my_set.remove(2)
# print(my_set)

# set1={1.1,2.2,3.3,4.4}
# set2={3.3,4.4,5.5,6.6}
# # print(set1.union(set2))
# print(set1.intersection(set2))

# dictionary
# dict={"table": ["a piece of furniture","list of facts and figures"], "cat":"a small animal"}
# print(dict)

# set question
# subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(subjects))

# dictionary question
# marks={}
# subject1=input("enter subject1 name:")
# marks.update({"subject1"})
# subject2=input("enter subject2 name:")
# marks.update({"subject2"})
# subject3=input("enter subject3 name:")
# marks.update({"subject3"})

# x=int(input("enter math marks:"))
# marks.update({"math":x})
# y=int(input("enter physics marks:"))
# marks.update({"physics":y})
# z=int(input("enter chemistry marks:"))
# marks.update({"chemistry":z})
# print(marks)

# set= set()
# set.add(("float",9.0))
# set.add(("int",9))
# print(set)
  
# while loop
# i=100
# while i>=1:
#     print(i)
#     i-=1

# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1/

# list1=[1,4,9,16,25,36,49,64,81,100]
# # i=0
# # while i<=len(list1)-1: 
# #     print(list1[i])
# #     i+=1 
# x=49
# i=0
# while i<=len(list1)-1:
#     if(list1[i]==x):
#         print("Element found at index:", i,x)
#     i+=1
# for loop
# tup=(1,2,3,4,5)
# for i in tup:
#     print(i)

# str="apnacallege"
# for char in str:
#     if(char=="o"):
#         print("o found")
#         break
#     print(char)
# else:
#     print("o not found")    

tup=(1,4,9,16,25,36,49,64,81,100)
x=100
idx=0
for i in tup:
    if(i==x):
        print("Element is:",x, "at ",idx)
        break
    print(i)
    idx+=1
else:
    print("element not found")