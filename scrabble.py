from wordscore import score_word, find_valid_words
import itertools


def run_scrabble(character):

    '''
    character: is the 
    '''
    
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]
        
    character = character.upper()
    valid = []            #valid scrabble words (score, word)
    total_number = 0
    
    wildcard = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wildcards = character.count('*') + character.count('?')
    without_wild = character.replace('*', '').replace('?', '')
    
    if len(character) > 7 or len(character) < 2:
        return "The input is not 2-7 characters"
    if not without_wild.isalpha() and len(without_wild) != 0:
        return "The input should only be letters"
    if character.count('*') + character.count('?') > 2:
        return "The number of wildcards are greater than 2"
    
    for i in range(wildcards + 1):
        
        if wildcards > 0:
            for letter in wildcard:
                temp = character.replace('*', letter).replace('?', letter)
                valid_words = find_valid_words(temp, data)
                for word in valid_words:
                    score = score_word(without_wild)
                    if not word in valid:
                        valid.append((score, word))
                    total_number += 1
            wildcards -= 1
            if wildcards == 0:
                break

        
        else:
            valid_words = find_valid_words(character, data)
            for word in valid_words:
            #print(word)
                score = score_word(word)
                valid.append((score, word))
                total_number += 1
                
    if character.count('*') + character.count('?') > 0 and len(find_valid_words(without_wild, data)) > 0: 
        word_scores = {}
        for score, word in valid:
            if word not in word_scores or score > word_scores[word]:
                word_scores[score] = word

        sorted_words = sorted(word_scores.items(), key=lambda x: (-x[0], x[1]))
        return sorted_words, total_number
    else:
        valid.sort(key=lambda x: (-x[0], x[1]))
        return valid, total_number