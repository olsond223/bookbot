def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    chars_dict = {}
    for character in file_contents:
        lcharacter = character.lower()
        if lcharacter not in chars_dict:
            chars_dict[lcharacter] = 1
        else:
            chars_dict[lcharacter] += 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(chars_dict):
    char_list = []
    for character in chars_dict:
        char_dict = {}
        char_dict["char"] = character
        char_dict["num"] = chars_dict[character]
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
