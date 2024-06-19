def num_to_binary(number, bits):
    bin_num = ""
    for bit in range(bits - 1, -1, -1):
        if number >= 2 ** bit:
            bin_num += '1'
            number -= 2 ** bit
        else:
            bin_num += '0'
    print("the num 5 in binary " , bin_num)
    return bin_num
    
x =num_to_binary(5, 8)
print(x)
def num_to_negBin(bin_num,bits):
    neg_bin_num = ""
    for i in range(bits):
        if bin_num[i] == '0':
            neg_bin_num += '1'
        else:
            neg_bin_num += '0'
    
    print("the !binary num is: ",bin_num)
    #add one to the !binary
    carry = 1
    neg_bin_num = list(neg_bin_num)
    for i in range(bits-1,-1,-1):
        if neg_bin_num[i] == '0' and carry==1:
            neg_bin_num[i] = '1'
            carry = 0
        elif neg_bin_num[i] == '1' and carry==1:
            neg_bin_num[i] = '0'
        else:
            break
    neg_bin_num = ''.join(neg_bin_num)
    print("The !binary + 1 is: ", neg_bin_num)
    return neg_bin_num
num_to_negBin(num_to_binary(5, 8),8)