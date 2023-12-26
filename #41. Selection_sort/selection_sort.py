list1=[38,56,75,78,34,23,112,89,90]
n=len(list1)

for i in range(n):
     
     min_ind=i
     for j in range(i+1,n):
          if list1[min_ind]>list1[j]:
               min_ind=j
     list1[i],list1[min_ind]=list1[min_ind],list1[i]

print("Selection Sort")
print(list1)              



