def encryptMessage(arr):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in arr:
        if isPrime(num):
            result.append("*")
        else:
            result.append(str(num))
    return " ".join(result)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(encryptMessage(arr))
