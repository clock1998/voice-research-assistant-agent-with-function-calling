def create_domain_specific_prompt(background_info: str) -> str:
    """
    Create prompt for domain-specific technical questions
    """
    domain_prompt = f"""Based on this technical background, create a specific technical interview question:

Background: {background_info}

Requirements:
- Test deep technical knowledge
- Include specific technologies/versions
- Require concrete examples
- Show real-world application

Format as JSON: {{"question": "...", "answer": "..."}}"""
    
    return domain_prompt

# Example usage
background = "Experience with React hooks and state management in large-scale applications"
prompt = create_domain_specific_prompt(background)
print("Domain-Specific Prompt:")
print(prompt)