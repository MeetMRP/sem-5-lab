def booth_multiplication(Q, M):
    # Converting Q and M to binary
    def to_binary(num, length):
        if num < 0:
            return bin(((1 << length) + num)).replace('0b', '').replace('-', '')
        return bin(num).replace('0b', '').replace('-', '').zfill(length)

    # Calculating the number of bits
    n = max(Q.bit_length(), M.bit_length()) + 1

    # Initializing registers
    A = 0
    Q_1 = 0

    # Performing the algorithm
    for _ in range(n):
        if (Q & 1) == 1 and Q_1 == 0:
            A = A - M
        elif (Q & 1) == 0 and Q_1 == 1:
            A = A + M

        # Right Shift
        Q_1 = Q & 1 
        Q = (Q >> 1) | ((A & 1) << (n - 1))
        A = (A & (1 << n)) | (A >> 1)

    # Combining A and Q for the result
    result = (A << n) | Q
    if result & (1 << (2 * n - 1)):
        result -= 1 << (2 * n)

    # Converting result to binary
    result_bin = to_binary(result, 2 * n)
    return result_bin, result


print(booth_multiplication(33, 4))