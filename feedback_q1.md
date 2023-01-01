Initialise the seed using np.random.seed

In the class Tester, there are following issues in the functions: 

1. def iterative_mult(w) :
* You were trying to apply the conventional matrix multiplication algorithm here, which is not necessary since w is a row vector. So one for loop is unnecessary
* You were also supposed to find sum of all elements, which is missing
* You weren't supposed to return the time, you had to return the sum of all elements.

2. def matrix_mult(w) :
* Similar comments as 1.

3. def comparison(w) :
* You needed to copy paste the last part of your code of both functions here

4. Plotting
* Looks good, the inputs are in powers of 10, so plotting on a logarithmic scale makes sense here.

Good work on the observations.
