def score_word(word):
    '''
    word: is the word you want to check its score
    '''
    
    score = 0
    word = word.lower()
    print(word)
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    
    for i in word:
        if i in scores:
            score += scores[i]
    
    return score

def find_valid_words(rack, word_list):
    valid_words = []

    rack_list = list(rack)
    # Iterate through each word in the word list
    for word in word_list:
        rack_copy = rack_list[:]
       
        can_form_word = True
        for letter in word:
            
            if letter in rack_copy:
                # Remove the letter from the rack to handle repeat letters
                rack_copy.remove(letter)
            else:
                # If the letter is not in the rack, mark the word as unable to form
                can_form_word = False
                break  # No need to continue checking the rest of the letters
        # If all letters in the word are found in the rack, add the word to the valid_words list
        if can_form_word:
            valid_words.append(word)

    return valid_words