# --- Data ---
# A small collection of documents (our corpus)
corpus = [
    'URGENT! You have won a 1 week FREE membership in our prize jackpot.',
    'Hey, what time is the meeting tomorrow?',
    'WINNER!! As a valued network customer you have been selected to receive a prize.',
    'Are you coming to the party tonight?',
    'Congratulations! You won a free flight to Bahamas.'
]

def clean_text(text):
    """A helper function to clean text by making it lowercase and removing punctuation."""
    text = text.lower()
    # Simple punctuation removal
    for punc in '.,?!':
        text = text.replace(punc, '')
    return text

# --- Functions to Implement ---

def build_vocabulary(corpus):
    word_set = set()
    
    for doc in corpus:
        cleaned_doc = clean_text(doc)
        words = cleaned_doc.split()
        
        word_set.update(words)
        
    return sorted(list(word_set))


def vectorize_text(text, vocabulary):
    vector = [0] * len(vocabulary)
    
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    for word in words:
        if word in vocabulary:
            index = vocabulary.index(word)
            vector[index] += 1
            
    return vector


# --- Main Execution ---
if __name__ == '__main__':
    # 1. Build the vocabulary from the corpus
    vocabulary = build_vocabulary(corpus)
    print(f"Vocabulary ({len(vocabulary)} words):")
    print(vocabulary)
    print("-" * 30)

    # 2. Vectorize each document in the corpus
    print("Vectorized Corpus:")
    for doc in corpus:
        vector = vectorize_text(doc, vocabulary)
        print(f"Original: {doc}")
        print(f"Vector:   {vector}\n")
