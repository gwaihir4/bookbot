def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict.update({char:1})
    return char_dict

def sort_on (dict_list):
    return  dict_list["num"] 

def sorted_list(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"char":char, "num":dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    for dict in dict_list:
        print (f"{dict["char"]}: {dict["num"]}")

def get_book_text(filepath):
    with open (filepath) as f:
        contents = f.read()
    return contents
