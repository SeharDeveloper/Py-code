import re
from collections import Counter

def word_frequency_counter(text):
    # Convert text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    #Split text into words
    words = text.split()
    
    #define a set of common words to ignore 
    common_words = {'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'at', 'on', 'for', 'with'}
    
    #Filter out common words
    filtered_words = [word for word in words if word not in common_words]
    
    #Count word frequencies using Counter
    frequency = Counter(filtered_words)
    
    #Create a set of unique words
    unique_words = set(filtered_words)
    
    #Find the most frequent word
    most_frequent_word = frequency.most_common(1)[0][0] if frequency else None
    
    #Return results as a dictionary
    result = {
        'frequency': dict(frequency),
        'unique_words': unique_words,
        'most_frequent_word': most_frequent_word
    }
    
    return result
text = "The quick brown fox jumps over the lazy dog. The dog barks back at the fox."
result = word_frequency_counter(text)
print(result)