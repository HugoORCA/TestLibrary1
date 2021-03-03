from math import sqrt

class serie:
    def sum_N(self, N):
        s=0
        for i in range(N):
            s += i
        return s

    def sum_sqrtN(self, N):
        s=0
        for i in range(N):
            s += sqrt(i)
        return s