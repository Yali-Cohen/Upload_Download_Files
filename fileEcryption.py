def input_file():
    print("hello")

input_file()

def print_bits_from_file(file_path):
    with open(file_path, 'rb') as file:
        byte = file.read(1)
        while byte:
            byte_value = ord(byte)  # Convert byte to integer
            bits = f'{byte_value:08b}'  # Convert to 8-bit binary string
            for bit in bits:
                print(bit, end=' ')
            print()
            byte = file.read(1)

# Example usage
print_bits_from_file('keylogger.txt')
