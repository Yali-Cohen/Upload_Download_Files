def vowels(st):
    st = st.lower()
    counter_vowels = 0
    for char in st:
        if char in {'a', 'e', 'i', 'o', 'u'}:
            counter_vowels += 1
    print(f"The times that vowel letters appeared: {counter_vowels}")

st = "Hello, world! My name is YaliI"
vowels(st)
