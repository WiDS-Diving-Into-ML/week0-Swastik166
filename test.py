import numpy as np
from time import time

'''w = np.random.randn(1, 10000)
M = np.random.randn(10000, 100)
def first(w, M):
    start_time1 = time()
    ans_row = len(w)
    ans_col = len(M[0])
    M1 = np.zeros((ans_row, ans_col))

    for i in range(ans_row):
        for j in range(ans_col):
            s = 0
            for k in range(len(M)):
                s += w[i][k] * M[k][j]
            M1[i,j] = s
    end_time1 = time()
    t1 = end_time1 - start_time1
    #print(t1)
    #print(M1)
    return(t1, M1)

def second(w,M):
    start_time2 = time()
    M2 = np.dot(w, M)
    end_time2 = time()
    t2 = end_time2 - start_time2
    #print(t2)
    #print(M2)
    return(t2, M2)



t1, M1 = (first(w,M))
t2, M2 = (second(w,M))
print(t1, t2, M1, M2)
print((M1 == M2))'''



w = np.random.randn(1,100)
M = np.random.randn(100, 10000)
start = time()
M2 = np.dot(w, M)
end = time()
print(end - start)