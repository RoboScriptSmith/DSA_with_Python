def Quick_Sort(list1):
     if len(list1)<=1:
          return list1
     else:
          pivot=list1[0]
          lesser=[x for x in list1[1:] if x<=pivot]
          grater=[x for x in list1[1:] if x>pivot]

          return Quick_Sort(lesser)+[pivot]+Quick_Sort(grater)     


my_list=[53,11,72,68,41,25,18,37,44,80]

my_list=Quick_Sort(my_list)

print(my_list)