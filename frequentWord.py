def readFile():
    file_path = createFile()
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
    list_to_dictionary(words)
def createFile():
    try:
        file_path = input_file()
    except KeyboardInterrupt:
        print("wrong file name")
    except FileNotFoundError:
        print("this file isn't exist")
    with open(file_path,'w') as file:
        file.write("hello world, my name is yali and my name is levy levy levy")
    return file_path
def input_file():
    file_path = input("Enter the path of the file you want ")
    return file_path
def list_to_dictionary(words):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print(counter)
    items = counter.items()
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)
readFile()


    