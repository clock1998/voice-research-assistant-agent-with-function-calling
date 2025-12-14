import random
from typing import List


behavioral_templates = [
    "Tell me about a time when you had to learn a new technology quickly",
    "Describe a challenging debugging session you've had",
    "How do you handle conflicting priorities in your work?",
    "Explain a technical concept to a non-technical person",
    "Tell me about a time you disagreed with a technical decision",
    "How do you approach code reviews?",
    "Describe a project where you had to work with a difficult stakeholder",
    "Tell me about a time you made a mistake in production"
]

def generate_behavioral_questions(templates: List[str], count: int = 5) -> List[str]:
    """
    Generate behavioral questions from templates
    """
    return random.sample(templates, min(count, len(templates)))

# Generate sample behavioral questions
behavioral_questions = generate_behavioral_questions(behavioral_templates)
print("Sample Behavioral Questions:")
for i, question in enumerate(behavioral_questions, 1):
    print(f"{i}. {question}")