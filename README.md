
# Spelling corrector and grammar checker for Tamil

This is a Natural Language Project (AI) used to ensure that a sentence contains correct words and correct grammar.



## Authors

- [Sathurshan.P](https://github.com/SathurshanPrabaharan)

- [Kapishothman.P](https://github.com/Kapisothman)


<!-- ## Environment Setup

### Check the python version
```
python --version
```

[//]: # (### Clone the indic_nlp library & resources)

[//]: # (```)

[//]: # (mkdir indic_nlp)

[//]: # (cd indic_nlp)

[//]: # (git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git)

[//]: # (git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git)

[//]: # ()
[//]: # (```)

### Install necessary libraries


```
pip install python-Levenshtein
pip install indic-nlp-library
pip install transformers

pip install indic-tokenizer

# for pretrained models
pip install torch




``` -->

# 01. Rule-Based Grammar Checker

Here, we use a Python NLP library called [`stanza`](https://github.com/stanfordnlp/stanza) to process Tamil sentences.\
This library provides many useful features:

<details>
<summary>1. Tokenization</summary>

* **Processor**: `tokenize`  
* **Description**: Splits text into sentences and tokens (words).  
* **Example Output**:  
    - Sentence: "நான் புத்தகம் வாசிக்கிறேன்."
    - Tokens: ["நான்", "புத்தகம்", "வாசிக்கிறேன்", "."]

</details>

<details>
<summary>2. Part-of-Speech Tagging</summary>

* **Processor**: `pos`  
* **Description**: Assigns part-of-speech tags (e.g., noun, verb, adjective) to tokens.  
* **Example Output**:  
    - "நான்" → "PRON"
    - "புத்தகம்" → "NOUN"  
* [Click here to view all UPOS tags](https://universaldependencies.org/u/pos/)

</details>

<details>
<summary>3. Lemmatization</summary>

* **Processor**: `lemma`  
* **Description**: Returns the base or dictionary form of a word (lemma).  
* **Example Output**:  
    - Input → "வாசிக்கிறேன்"  
    - Output → "வாசி"

</details>

<details>
<summary>4. Dependency Parsing</summary>

* **Processor**: `depparse`  
* **Description**: Identifies grammatical relations between words, forming a dependency tree.  
* **Example Output**:  
    - Input: "நான் புத்தகம் வாசிக்கிறேன்"  
        - நான் → Subject  
        - வாசிக்கிறேன் → Root  
        - புத்தகம் → Object  

</details>







## Reference/Resource
- [indic-nlp-library](https://pypi.org/project/indic-nlp-library/)
- [Indic NLP Resources](https://github.com/anoopkunchukuttan/indic_nlp_resources)