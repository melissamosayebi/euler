def maz(a):
   mazrab=False 
   if a%3==0 or a%5==0:
       mazrab=True
   return mazrab
j=0
for i in range(1000):
   if maz(i):
       j+=i
print(j)       