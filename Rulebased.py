import re

# Define tense-specific verb suffixes
present_tense_suffixes = ['கிறான்', 'கிறேன்', 'கிறார்கள்', 'கிறது']
past_tense_suffixes = ['னான்', 'னாள்', 'னார்கள்', 'னது']
future_tense_suffixes = ['வான்', 'வாள்', 'வார்கள்', 'வது', 'பேன்', 'வேன்']
object_suffixes = ['க்கு', 'ம்', 'இல்', 'ஆல்', 'வை']

# Define singular and plural subjects with suffixes
singular_subjects = ['அவன்', 'அவள்', 'நான்', 'அது']
plural_subjects = ['நீ', 'அவர்கள்', 'அவை', 'இவை']

# Plural subject suffixes (e.g., for words like 'அவர்கள்', 'இவர்கள்')
plural_subjects_suffixes = ['கள்']

# Load subject words from multiple files
def load_subject_words(file_paths):
    subject_words = set()  # Using a set to avoid duplicates
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                subject_words.update(line.strip() for line in file if line.strip())
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
    return list(subject_words)

# Step 1: Classify word based on suffix rules and tense
def classify_word(word, subject_words):
    # Check for present tense verbs
    for suffix in present_tense_suffixes:
        if word.endswith(suffix):
            return 'VERB_PRESENT'
    # Check for past tense verbs
    for suffix in past_tense_suffixes:
        if word.endswith(suffix):
            return 'VERB_PAST'
    # Check for future tense verbs
    for suffix in future_tense_suffixes:
        if word.endswith(suffix):
            return 'VERB_FUTURE'
    # Check for subjects
    if word in subject_words:
        return 'SUBJECT'
    # Check for plural subjects (suffix matching)
    for suffix in plural_subjects_suffixes:
        if word.endswith(suffix):
            return 'SUBJECT_PLURAL'
    # Check for objects
    for suffix in object_suffixes:
        if word.endswith(suffix):
            return 'OBJECT'
    return 'UNKNOWN'

# Step 2: POS tagging for a list of tokens
def pos_tagging_custom(tokens, subject_words):
    pos_tags = []
    for token in tokens:
        tag = classify_word(token, subject_words)
        pos_tags.append((token, tag))
    return pos_tags

# Step 3: Split paragraph into sentences
def split_into_sentences(paragraph):
    # Split sentences based on Tamil punctuation or English full stops
    sentences = re.split(r'(?:[.!?]|[।])\s*', paragraph)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Step 4: Tokenize sentences into words
def tokenize_sentence(sentence):
    return sentence.split()

# Step 5: Apply grammar correction rules (including subject-verb agreement)
def apply_grammar_rules(pos_tags):
    corrected_sentence = []
    for i, (word, tag) in enumerate(pos_tags):
        if tag == 'SUBJECT' and i + 1 < len(pos_tags):
            next_word, next_tag = pos_tags[i + 1]
            # Check if next word is a verb (and check subject-verb agreement)
            if next_tag.startswith('VERB'):
                # Validate singular/plural agreement for subject-verb
                if word in singular_subjects and next_word.endswith('னான்'):  # Singular
                    corrected_sentence.append(word)
                    corrected_sentence.append(next_word)
                elif word in plural_subjects and next_word.endswith('னர்'):  # Plural
                    corrected_sentence.append(word)
                    corrected_sentence.append(next_word)
                else:
                    corrected_sentence.append(word)
                    corrected_sentence.append("முடிவற்ற")  # Add placeholder if verb doesn't match
            else:
                corrected_sentence.append(word)
                corrected_sentence.append(next_word)
        elif tag == 'SUBJECT_PLURAL' and i + 1 < len(pos_tags):
            next_word, next_tag = pos_tags[i + 1]
            # For plural subjects, ensure the verb is in plural form (checks for plural verb ending)
            if next_tag.startswith('VERB'):
                if next_word.endswith('னர்'):  # Correct plural verb form
                    corrected_sentence.append(word)
                    corrected_sentence.append(next_word)
                else:
                    corrected_sentence.append(word)
                    corrected_sentence.append("முடிவற்ற")  # Placeholder for incorrect verb form
            else:
                corrected_sentence.append(word)
                corrected_sentence.append(next_word)
        else:
            corrected_sentence.append(word)
    return " ".join(corrected_sentence)

# Step 6: Process the entire paragraph
def process_paragraph(paragraph, subject_words):
    sentences = split_into_sentences(paragraph)  # Split into sentences
    corrected_paragraph = []
    for sentence in sentences:
        tokens = tokenize_sentence(sentence)  # Tokenize each sentence
        pos_tags = pos_tagging_custom(tokens, subject_words)  # Perform POS tagging
        corrected_sentence = apply_grammar_rules(pos_tags)  # Apply grammar rules
        corrected_paragraph.append(corrected_sentence)
    return " ".join(corrected_paragraph)

# Main Function
if __name__ == "__main__":
    # List of subject word files
    subject_files = ["D:\\Study\\New folder\\Tamil Corpora\\all-tamil-nouns.txt"]
  # You can add more files here
    subject_words = load_subject_words(subject_files)

    if not subject_words:
        print("No subject words loaded. Please check the subject files.")
    else:
        # Input paragraph with different tenses
        paragraph = """
        அவன் பள்ளிக்கு போகின்றான். அவள் பள்ளிக்கு போவாள். அவைகள் பள்ளிக்கு போகின்றன.
        """
        # Process and correct the paragraph
        corrected_paragraph = process_paragraph(paragraph, subject_words)
        print("Corrected Paragraph:")
        print(corrected_paragraph)
