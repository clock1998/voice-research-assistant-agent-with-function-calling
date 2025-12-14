from typing import List, Dict, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_diversity_score(questions: List[str]) -> float:
    """
    Calculate diversity score using TF-IDF vectorization
    Higher score = more diverse questions
    """
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(questions)
    similarities = cosine_similarity(tfidf_matrix)
    
    # Average pairwise similarity (excluding diagonal)
    avg_similarity = np.mean(similarities[np.triu_indices_from(similarities, k=1)])
    diversity_score = 1 - avg_similarity  # Higher = more diverse
    return diversity_score

# Test with sample questions
sample_questions = [
    "What is your experience with Python?",
    "Tell me about a challenging debugging session",
    "How do you handle API rate limiting?",
    "Explain microservices architecture",
    "Describe your testing methodology"
]

diversity = calculate_diversity_score(sample_questions)
print(f"Diversity Score: {diversity:.3f}")