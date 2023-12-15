def restoring_division(dividend, divisor):
    # Number of bits for shifting
    n = max(dividend.bit_length(), divisor.bit_length())

    # Initialize the remainder and quotient
    remainder = 0
    quotient = 0

    # Extending the dividend to twice its size by left-shifting
    extended_dividend = dividend << n

    for i in range(n):
        # Extracting the most significant bit and appending to remainder
        remainder = (remainder << 1) | ((extended_dividend & (1 << (n*2 - 1))) >> (n*2 - 1))
        extended_dividend <<= 1  # Shifting the extended dividend for the next round

        # Subtracting divisor from remainder
        temp_remainder = remainder - divisor

        if temp_remainder >= 0:
            remainder = temp_remainder
            quotient = (quotient << 1) | 1  # Set LSB of quotient to 1
        else:
            quotient <<= 1  # Keep LSB of quotient as 0

    return quotient, remainder

# Testing the function
print(restoring_division(17, 3))

