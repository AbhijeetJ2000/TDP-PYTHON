if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))
    a = 0
    b = 1
    print("Fibonacci Series: ", a, b, end=" ")
    for i in range(2, n):
        next = a + b
        a = b
        b = next
        print(next, end=" ")



