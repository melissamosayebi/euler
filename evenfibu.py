def fibu():
   a=[1,2]
   i=0
   j=i+2
   sum=2
   while True:
      a.append(a[i]+a[i+1])
      if a[j]<4000000:
         if a[j]%2==0:
            sum+=a[j]
         #print(a)
         i+=1
         j+=1
      else:
         break
   return sum
print(fibu(),sum)