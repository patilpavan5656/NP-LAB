def binary_addition(b, c, carry):
    result = []
    for i in range(len(b) - 1, -1, -1):
        bit_sum = int(b[i]) + int(c[i]) + int(carry)
        result.append(str(bit_sum % 2))
        carry = str(bit_sum // 2)
    return result[::-1], carry

def sender(a, n, checksum):
    max_len = max(len(x) for x in a)
    a = ['0' * (max_len - len(x)) + x for x in a]
    
    carry = '0'
    checksum_result = []
    
    for j in range(max_len):
        b = [x[j] for x in a]
        result, carry = binary_addition(b, ['0'] * n, carry)
        checksum_result.extend(result)
    
    checksum.extend(['1' if x == '0' else '0' for x in checksum_result])
    
    print("\nCarry =", carry, "\tChecksum =", "".join(checksum_result))

def receiver(a, n, checksum):
    max_len = len(a[0])
    
    carry = '0'
    
    for j in range(max_len):
        b = [x[j] for x in a]
        result, carry = binary_addition(b, ['0'] * n, carry)
    
    checksum_result = ['1' if x == '0' else '0' for x in result]
    
    if checksum_result != checksum:
        print("There is an error detected")
    else:
        print("There is no error detected")

def main():
    n = int(input("Enter the number of input strings: "))
    a = [input("Enter the input binary string: ") for _ in range(n)]
    checksum = []

    print("From Sender side.......")
    print("Input Strings are:")
    [print(x) for x in a]
    sender(a, n, checksum)

    print("\n\nFrom Receiver side for the checksum....... " + "".join(checksum))
    print(f"Enter {n} input strings:")
    a = [input("Enter the input binary string: ") for _ in range(n)]
    
    print("Input Strings are:")
    [print(x) for x in a]
    receiver(a, n, checksum)

if __name__ == "__main__":
    main()