translit_dictionary = {
    "а": "а", "б": "b", "в": "v", "г": "g", "д": "d",
    "е": "e", "ё": "e", "ж": "j", "з": "z", "и": "i",
    "й": "i", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "h", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "sh'", "ъ": "'", "ы": "i", "ь": "'",
    "э": "e", "ю": "u", "я": "ya"
}

input_string = input("Введите ваше предложение: ")
result_string = ""

for char in input_string:
    if char.lower() in translit_dictionary.keys():
        new_char = translit_dictionary[char.lower()]
    else:
        new_char = char

    if char.isupper():
        new_char = new_char.upper()

    result_string += new_char

print(result_string)
