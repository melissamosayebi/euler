import time
start=time.time()
def prime(x):
    is_prime=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_prime=False
            break
        else:
            is_prime=True
    return is_prime
a=600851475143 
i=3
while True:
    if a%i==0:
        f=a//i
        #print(lst)
        if prime(f):
            print(f)
            break
    i+=1
print("Run Time: " + str( time.time() - start ))