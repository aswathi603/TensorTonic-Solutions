import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    # Step 1: Handle empty input
    if not documents:
        return np.array([]), []
    
    # Step 2: Tokenize documents
    tokenized_docs = []
    for doc in documents:
        if doc.strip() == "":
            tokenized_docs.append([])
        else:
            tokenized_docs.append(doc.lower().split())
    
    N = len(tokenized_docs)
    
    # Step 3: Build vocabulary (sorted)
    vocab_set = set()
    for tokens in tokenized_docs:
        vocab_set.update(tokens)
    
    vocabulary = sorted(vocab_set)
    vocab_index = {word: i for i, word in enumerate(vocabulary)}
    
    V = len(vocabulary)
    
    # Step 4: Compute document frequency (df)
    df = Counter()
    for tokens in tokenized_docs:
        unique_terms = set(tokens)
        for term in unique_terms:
            df[term] += 1
    
    # Step 5: Compute IDF
    idf = {}
    for term in vocabulary:
        if df[term] > 0:
            idf[term] = math.log(N / df[term])
        else:
            idf[term] = 0.0
    
    # Step 6: Initialize TF-IDF matrix
    tfidf_matrix = np.zeros((N, V))
    
    # Step 7: Compute TF-IDF
    for doc_idx, tokens in enumerate(tokenized_docs):
        if not tokens:
            continue
        
        term_counts = Counter(tokens)
        total_terms = len(tokens)
        
        for term, count in term_counts.items():
            if term in vocab_index:
                tf = count / total_terms
                tfidf_matrix[doc_idx, vocab_index[term]] = tf * idf[term]
    
    return tfidf_matrix, vocabulary