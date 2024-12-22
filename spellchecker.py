# -*- coding: utf-8 -*-
"""spellchecker.ipynb

import re
from difflib import get_close_matches
from collections import defaultdict

# Function to load words from multiple .txt files
def load_words_from_files(file_paths):
    words = set()
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    words.add(line.strip().replace(" ", ""))  # Add cleaned words
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
    return words

# Function to generate n-grams from a word
def generate_ngrams(word, n=2):
    return [word[i:i+n] for i in range(len(word)-n+1)]

# Function to suggest corrections based on fuzzy matching and n-grams
def suggest_correction(word, word_list, ngram_dict, n=2):
    # Fuzzy matching: Get the closest matches for the word from the word list
    fuzzy_matches = get_close_matches(word, word_list, n=3, cutoff=0.7)  # Higher cutoff for relevant matches

    # If no fuzzy matches, use n-gram-based suggestions
    if not fuzzy_matches:
        word_ngrams = generate_ngrams(word, n)
        best_matches = defaultdict(int)
        for ngram in word_ngrams:
            for w in word_list:
                if ngram in generate_ngrams(w, n):
                    best_matches[w] += 1

        # Sort matches by count (the more n-grams match, the higher the score)
        best_matches = sorted(best_matches.items(), key=lambda x: x[1], reverse=True)
        fuzzy_matches = [match[0] for match in best_matches[:3]]

    return fuzzy_matches

# Function to process sentences/paragraphs and auto-correct
def auto_correct_paragraph(paragraph, word_list, ngram_dict):
    words = re.findall(r'[\u0B80-\u0BFF]+', paragraph)  # Split the paragraph into words

    auto_corrected_paragraph = paragraph
    for word in words:
        if word not in word_list:  # If the word is not in the dictionary
            corrections = suggest_correction(word, word_list, ngram_dict)  # Get suggestions
            if corrections:  # If suggestions are available
                correct_word = corrections[0]  # Use the first suggestion
                auto_corrected_paragraph = auto_corrected_paragraph.replace(word, correct_word)

    return auto_corrected_paragraph

# Step 1: Define the paths of the .txt files you want to load
file_paths = [
    '/content/drive/MyDrive/AI/para.txt',
    '/content/drive/MyDrive/AI/numbers.txt',
    '/content/drive/MyDrive/AI/paragraph (1).txt'
]

# Step 2: Load the dictionary from all specified .txt files
word_list = load_words_from_files(file_paths)

# Step 3: Generate n-grams for the word list
ngram_dict = {}
for word in word_list:
    ngram_dict[word] = generate_ngrams(word)

# Step 4: Get input from the user
paragraph_to_check = input("Enter a paragraph in Tamil: ")

# Step 5: Auto-correct the paragraph
auto_corrected_paragraph = auto_correct_paragraph(paragraph_to_check, word_list, ngram_dict)

# Step 6: Display the auto-corrected paragraph
print("\nAuto-corrected Paragraph:")
print(auto_corrected_paragraph)
