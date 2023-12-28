def partition(a,s,e):
     pivot=a[e]
     i=s-1

     for j in range(s,e):
          if a[j]<=pivot:
               i=i+1
               a[i],a[j]=a[j],a[i]
     a[i+1],a[e]=a[e],a[i+1]
     return i+1

     

def Quickprocess(a,s,e):
     if s<e:
          p=partition(a,s,e)
          Quickprocess(a,s,p-1)
          Quickprocess(a,p+1,e)


a=[3,5,6,1,2,4,9]
Quickprocess(a,0,len(a)-1)
print(a)


     
