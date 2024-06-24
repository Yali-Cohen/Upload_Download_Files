import sys

def readFile():
    if len(sys.argv) < 3:
        sys.exit(1)
    
    file_path = createFile()
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
    list_to_dictionary(words)

def createFile():
    try:
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = input("Enter the path of the file you want: ")
    except IndexError:
        print("No file name provided")
        sys.exit(1)
    
    with open(file_path, 'w') as file:
        file.write("hello world, my name is yali and my name is levy levy levy")
    return file_path

def list_to_dictionary(words):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    try:
        if len(sys.argv) > 2:
            N = int(sys.argv[2])
        else:
            N = int(input("Enter the number of top words to display: "))
    except IndexError:
        print("No number provided for N")
        sys.exit(1)
    except ValueError:
        print("Invalid number provided for N")
        sys.exit(1)
    
    print(f"Top {N} words:")
    for i in range(min(N, len(sorted_items))):
        print(sorted_items[i][0])

if __name__ == "__main__":
    readFile()
