

    

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