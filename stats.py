def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(input):
    return len(input.split())

def get_char_count(input):
    char_count = {}
    for char in input.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def list_char_count(num_char):
    num_char = get_char_count(num_char)
    list = []
    for char in num_char:
        list.append({"char": char, "num": num_char[char]})
    list.sort(reverse=True, key=sort_on)
    return list
