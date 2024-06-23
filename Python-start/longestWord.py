def find_longest_word(ls):
    length_longest = 0 
    for word in ls:
        if len(word)>length_longest:
            length_longest = len(word)
    for word in ls:
        if len(word) == length_longest:
            return word
    
words_list = input("Enter words separated by spaces: ").split()
print(f"the longest word is {find_longest_word(words_list)}")