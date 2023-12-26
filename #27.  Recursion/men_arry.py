import array as arr
def mean_array(a,n):
     if(n==-1):
          return 0
     s=a[n]+mean_array(a,n-1)
     return s


a = arr.array('i', [1, 2, 3])

l=len(a)  
r=mean_array(a,l-1)
result=int(r/l)
print(r)

print(l)
print(result)