list1=[38,56,75,78,34,23,12,89,90]
n=len(list1)

for i in range(n-2):
     for j in range(n-1-i):
          if list1[j]>list1[j+1]:
               list1[j],list1[j+1]=list1[j+1],list1[j]

print(list1)