import time
a = time.time()
sum =0
for i in range(10,0,-1):
    print(i)
    sum =sum +i
print(sum)
b = time.time()
print(b-a)