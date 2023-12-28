class Graph:
     def __init__(self,vno):
          self.vertex_count=vno
          self.adj_matrix=[[0]*vno for i in range(vno)]

     def add_edge(self,u,v,weight=1):
          if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
               self.adj_matrix[u][v]=weight
               self.adj_matrix[v][u]=weight

          else:
               print("Invalid Graph")

     def has(self,u,v):
          return self.adj_matrix[v][u]!=0

     def delete_edge(self,u,v):
          if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
               self.adj_matrix[u][v]=0
               self.adj_matrix[v][u]=0

          else:
               print("Invalid Graph") 

     def print_adj_matrix(self):
          for row_list in self.adj_matrix:
               print(" ".join(map(str,row_list))) 

g1=Graph(6)

g1.add_edge(0,1)
g1.add_edge(0,2)
g1.add_edge(0,4)
g1.add_edge(2,4)
g1.add_edge(4,5)
g1.add_edge(5,3)
g1.add_edge(3,1)
g1.add_edge(0,3)

g1.print_adj_matrix()
                                