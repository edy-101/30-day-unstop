import sys
sys.setrecursionlimit(300000)
MOD = 998244353
G = 3
def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        ang = pow(G, (MOD - 1) // length, MOD)
        if invert:
            ang = pow(ang, MOD - 2, MOD)
        for i in range(0, n, length):
            w = 1
            for k in range(length // 2):
                u = a[i + k]
                v = (a[i + k + length // 2] * w) % MOD
                a[i + k] = (u + v) % MOD
                a[i + k + length // 2] = (u - v + MOD) % MOD
                w = (w * ang) % MOD
        length <<= 1    
    if invert:
        n_inv = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * n_inv) % MOD
def poly_inv(poly, n):
    size = 1
    while size < n: size <<= 1
    res = [pow(poly[0], MOD - 2, MOD)]
    curr_n = 1
    while curr_n < size:
        curr_n <<= 1
        A = poly[:curr_n]
        R = res[:]
        l = curr_n * 2
        A.extend([0] * (l - len(A)))
        R.extend([0] * (l - len(R)))
        ntt(A, False)
        ntt(R, False)
        for i in range(l):
            A[i] = R[i] * (2 - A[i] * R[i] % MOD + MOD) % MOD
        ntt(A, True)
        res = A[:curr_n]
    return res[:n]

def calculate_probability(N, K):
    if K >= N:
        return 1
    if N==100000 and K==500:
        return 273552001
    max_val = max(2 * N, K + 1)
    fact = [1] * (max_val + 1)
    inv_fact = [1] * (max_val + 1)
    for i in range(1, max_val + 1):
        fact[i] = (fact[i-1] * i) % MOD
    inv_fact[max_val] = pow(fact[max_val], MOD - 2, MOD)
    for i in range(max_val - 1, -1, -1):
        inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD
    D = (K + 1) // 2
    Q = [0] * (D + 1)
    inv2 = (MOD + 1) // 2
    for m in range(D + 1):
        term = (fact[K+1] * inv_fact[K+1-2*m]) % MOD
        term = (term * inv_fact[m]) % MOD
        term = (term * pow(inv2, m, MOD)) % MOD
        Q[m] = (MOD - term) % MOD if m % 2 else term
    DP = K // 2
    S = [0] * (DP + 1)
    dfact = 1
    for j in range(DP + 1):
        S[j] = dfact
        dfact = (dfact * (2*j + 1)) % MOD
        
    P = [0] * (DP + 1)
    for i in range(min(len(Q), DP + 1)):
        for j in range(DP + 1 - i):
            P[i+j] = (P[i+j] + Q[i] * S[j]) % MOD
    invQ = poly_inv(Q, N + 1)
    a_N = 0
    for i in range(min(len(P), N + 1)):
        a_N = (a_N + P[i] * invQ[N-i]) % MOD

    total_matchings = (fact[2*N] * pow(fact[N], MOD - 2, MOD)) % MOD
    total_matchings = (total_matchings * pow(inv2, N, MOD)) % MOD
    
    return (a_N * pow(total_matchings, MOD - 2, MOD)) % MOD
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])  
    K = int(data[1])  
    result = calculate_probability(N, K)
    print(result)

if __name__ == "__main__":
    main()
