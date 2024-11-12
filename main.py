def main():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    total_words = len(words)
    print(total_words)

def character_count(file_contents):
    char_dict = {}

    for character in file_contents:
        lcharacter = character.lower()
        if lcharacter in char_dict:
            char_dict[lcharacter] += 1
        else:
            char_dict[lcharacter] = 1
        
    return char_dict

def split_dict(char_dict):
    dict_list = [{"character": character, "count": count} for character, count in char_dict.items()]
    return dict_list

def sort_on(characters):
    return characters["count"]



file_contents = main()
characters = character_count(file_contents)
char_dict = split_dict(characters)
char_dict.sort(reverse=True, key=sort_on)
for i in char_dict:
    character = i["character"]
    count = i["count"]
    if character.isalpha():
        print(f"The \"{character}\" character was found {count} times")
print("--- End report ---")