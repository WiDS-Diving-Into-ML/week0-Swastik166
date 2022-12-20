import numpy as np
from time import time


w = np.random.randn(1, 10000)
class Tester : 

  def __init__(self, M) :  
    self.M = M

  def __len__(self):
         return len(self.M)

  def iterative_mult(self, w) :
    start_time = time()
    ans_row = len(w)
    ans_col = len(self.M[0])
    M1 = np.zeros((ans_row, ans_col))

    for i in range(ans_row):
      for j in range(ans_col):
        s = 0
        for k in range(len(self.M)):
            s += w[i][k] * self.M[k][j]
        M1[i,j] = s
    end_time = time()
    t1 = end_time - start_time 
    return(t1)
    ### INSERT CODE ABOVE ### 

  def matrix_mult(self, w) :
    start_time = time()
    M2 = np.dot(w, M)
    end_time = time()
    t2 = end_time - start_time
    return(t2)
    ### INSERT CODE ABOVE ###

  def comparison(self, w) :

    time_iterative = 0
    time_matrix = 0

    ### INSERT CODE BELOW  ###
    time_iterative = Tester.iterative_mult(self, w)
    time_matrix = Tester.matrix_mult(self, w)
    ### INSERT CODE ABOVE ###

    print('Time taken by iterative method : {time_iterative}\nTime taken by matrix method : {time_matrix}')

    return time_iterative, time_matrix





M = np.random.randn(10000, 100)
tester = Tester(M)
print(tester.comparison(M))