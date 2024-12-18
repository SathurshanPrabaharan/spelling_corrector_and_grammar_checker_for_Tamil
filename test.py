import Levenshtein
from transformers import pipeline

# Define a list of valid Tamil words (you can expand this)
dictionary = ['வணக்கம்', 'எப்படி', 'இருக்கிறீர்கள்', 'உங்களுடைய', 'நான்', 'தமிழ்']

# Function to get the closest word using Levenshtein distance
def get_closest_word(word, dictionary):
    closest_word = min(dictionary, key=lambda w: Levenshtein.distance(word, w))
    return closest_word

# Function for spelling correction
def correct_spelling(sentence, dictionary):
    corrected_sentence = []
    words = sentence.split()  # Split sentence into words
    for word in words:
        corrected_word = get_closest_word(word, dictionary)
        corrected_sentence.append(corrected_word)
    return ' '.join(corrected_sentence)

# Load a pre-trained transformer model for grammar correction
# (You need a pre-trained grammar correction model fine-tuned for Tamil)
grammar_corrector = pipeline('text2text-generation', model='your-tamil-grammar-model')

# Function for grammar correction
def correct_grammar(sentence):
    corrected_sentence = grammar_corrector(sentence)
    return corrected_sentence[0]['generated_text']

# Example usage
sentence = "வணக்கம, எப்படி இரர்க்கிறீர்கள்"
spelling_corrected = correct_spelling(sentence, dictionary)
grammar_corrected = correct_grammar(spelling_corrected)

print("Original Sentence:", sentence)
print("Spelling Corrected:", spelling_corrected)
print("Grammar Corrected:", grammar_corrected)
