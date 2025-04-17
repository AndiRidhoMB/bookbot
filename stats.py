def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    
    return char_counts


def sort_on_key(dict):
    character_count_list = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = value
        character_count_list.append(new_dict)
    
    character_count_list.sort(reverse=True, key=lambda item: item["count"])
    return character_count_list




