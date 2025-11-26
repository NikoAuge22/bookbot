def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    dictionary = {}
    lower_text = text.lower()
    # count each character
    for character in lower_text:
        # fill dictionary ('character' : 'numer')
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

def sorted_characters(origin):
    #created empty list of dictionaries
    lists = []
    
    # loop over each character in origin dictionary
    for char in origin:
        # set empty dictionary for first character
        char_dict = {}
        # set first key value pair
        char_dict["char"] = char
        # set second key value pair
        char_dict["num"] = origin[char]
        # add new dictionary to list of dictionaries
        lists.append(char_dict)
    # helper function
    def sort_on(items):
        return items["num"]
    # sort the list
    lists.sort(reverse=True, key=sort_on)
    return lists

