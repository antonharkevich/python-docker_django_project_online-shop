import numpy 

def solve_linear_system(A):
    n = A.shape[0]
    # forward trace
    for k in range(n - 1):
        main_element(A, k)
        for i in range(k + 1, n):
            q = A[i, k] / A[k, k]
            A[i, :] -= A[k, :] * q

    if numpy.any(numpy.diag(A) == 0):
        print('The system has infinite number of answers.')
        return
        
    x = numpy.array([0.0 for i in range(n)], float).transpose()
    for k in range(n - 1, -1, -1):
        x[k] = (A[k, -1] - sum([A[k, i] * x[i] for i in range(k, n)])) / A[k, k]
    print(['{:.4f}'.format(x[i]) for i in range(n)])


def main_element(A, k):
    temp = k + numpy.argmax(numpy.abs(A[k:, k]))
    if k != temp:
        A[k, :], A[temp, :] = numpy.copy(A[temp, :]), numpy.copy(A[k, :])


A = numpy.array([[3.93, 0.81, 2.27, 0.92, -0.53, 4.2], 
    [-0.53, 3.93, 0.81, 2.27, 0.92, 4.2], 
    [2.52, -0.53, 3.93, 0.81, 2.27, 4.2], 
    [0.67, 2.52, -0.53, 3.93, 0.81, 4.2], 
    [0.81, 0.67, 2.52, -0.53, 3.93, 4.2]], float)

solve_linear_system(A)
