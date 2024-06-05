def num_to_binary(number, bits):
    bin_num = ""
    for bit in range(bits - 1, -1, -1):
        if number >= 2 ** bit:
            bin_num += '1'
            number -= 2 ** bit
        else:
            bin_num += '0'
    print(bin_num)
num_to_binary(5, 8)

def num_to_negBin(bin_num,bits):
    for i in range(bits):#not to the number
        if bin_num[i] == '0':
            bin_num[i] = bin_num[:i] + "1" + bin_num[i+1:]
        else:
            bin_num[i] = '0'
    print(bin_num)
    print("hi")
num_to_negBin(num_to_binary(5, 8),8)