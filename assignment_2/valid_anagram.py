def is_valid_anagram(word1, word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    # Compare the sorted strings
    return sorted_word1 == sorted_word2


word1 = "danger"
word2 = "garden"
result = is_valid_anagram(word1, word2)
print(result)
