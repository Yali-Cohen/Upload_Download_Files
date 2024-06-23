def find_palindromes(ls):
    ls_palindromes = []
    for word in ls:
        if word == word[::-1]:
            ls_palindromes.append(word)
    return ls_palindromes

words_list = input("Enter words separated by spaces: ").split()
print(find_palindromes(words_list))
