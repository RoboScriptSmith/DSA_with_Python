def sum(n):
     if n==1:
          return 1
     s=n+sum(n-1)
     return s


n=int(input("Enter N natural Number: "))
result=sum(n)
print("Sum of N natural Numbers: ",result)          