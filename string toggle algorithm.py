## question 
# Convert one string to another by toggling one character at a time.
# Each intermediary word formed should also be a word in the english dictionary
# (provided to you in the form of a Set/Dictionary).
# Return the series of words, in order, in any data structure of your choice.
# Eg.
# Problem: Convert “cat” to “dog”
#  Input: String “cat”, String “dog”, Set englishDictionary
# Output: “cat” → “cot” → “dot” → “dog” (stored in any data structure of your choice)
#solve this problem using a breadth-first search algorithm
from collections import deque

def convert_string(start, end, english_dict):
    queue = deque([start])
    visited = {start}

    while queue:
        word = queue.popleft()
        if word == end:
            return list(visited)
        
        for i in range(len(word)):
            for j in range(26):
                char = chr(ord('a') + j)
                next_word = word[:i] + char + word[i+1:]
                if next_word in english_dict and next_word not in visited:
                    queue.append(next_word)
                    visited.add(next_word)

    return []
