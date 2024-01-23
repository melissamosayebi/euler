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
i=8462696834
while i>2:
    if a%i==0:
        print(i)
        if prime(i):
            #print(i)
            s=i
            print(s)
            break 
            #print(f"c is {count}")
        i-=1000000000
    i-=1
#print(s) 
#600851475143   
#10000000000    
