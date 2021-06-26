def Monotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


if __name__ == '__main__':
    A = [6, 5, 4, 4]
    B = [5, 15, 20, 10]
    print(Monotonic(A))
    print(Monotonic(B))
