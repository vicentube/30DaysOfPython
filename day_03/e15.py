matching_word = 'on'
word1 = 'python'
word2 = 'dragon'
no_coincidence = not (matching_word in word1) and not (matching_word in word2)
print('There is no \'', matching_word, '\' in both', word1, 'and', word2, ':', no_coincidence)