L = 100000
M = [0] * (L + 1)
M0 = [0] * (L + 1)
M0[0] = 1
for i in range(1, L + 1):
    for j in range(0, L + 1):
        M[j] += M0[j]
        if j - i >= 0:
            M[j] += M[j - i]
    if i % 100 == 0:
        print("Processed", i)
    print(M)
    if M[i] % 100000 == 0:
        print(i, M[i])
    if M[i] % 1000000 == 0:
        print("Answer",i, M[i])
        quit()
    M0 = M
    M = [0] * (L + 1)
