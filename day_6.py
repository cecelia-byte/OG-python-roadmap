# multithreading
import threading
import time
# def helloworld():
#     print("helloworld")
# t1=threading.Thread(target=helloworld)
# t1.start()
# def function1():
#     for x in range(10):
#         print("hello")
# def function2():
#     for x in range (10):
#         print("world")

# t2=threading.Thread(target=function1)
# t3=threading.Thread(target=function2)
# t2.start()
# t3.start()
# def hello():
#     for x in range(10):
#         print("hello")
# t4=threading.Thread(target=hello)
# t4.start()
# t4.join()
# print("another text")
# print(threading.current_thread().name)
# def display(n,msg):
#     for i in range(n):
#         print(msg)
# t1=threading.Thread(target=display,kwargs={'n':4,'msg':"hello"})
# t1.start()
# print(time.time())
import numpy as np
# # import pandas
# a=[1,2,3,4,5]*1000
# b=np.array(a)
# start=time.time()
# new_b=b*2
# print(time.time()-start)
myarr=np.array([3,6,9,7])
print(myarr)