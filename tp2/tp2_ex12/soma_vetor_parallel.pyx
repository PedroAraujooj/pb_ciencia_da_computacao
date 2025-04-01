from cython.parallel cimport prange
import cython

def soma_vetor_parallel(double[:] vet):
    cdef int i
    cdef Py_ssize_t n
    cdef double total = 0.0
    n = vet.shape[0]
    for i in prange(n, nogil=True):
        total += vet[i]

    return total

