from typing import Dict


scenarios = [
    "Your application is running slowly in production",
    "You need to integrate with a third-party API that has rate limits",
    "You discover a security vulnerability in your codebase",
    "A critical service is down and customers are complaining",
    "Your database is approaching storage limits",
    "You need to migrate a legacy system to modern architecture",
    "A team member pushes breaking changes to main branch",
    "Your application needs to scale to 10x current traffic"
]

def create_scenario_question(scenario: str) -> Dict[str, str]:
    """
    Create a structured scenario-based question
    """
    question = f"Scenario: {scenario}. How would you approach this situation? Walk me through your problem-solving process."
    
    return {
        "scenario": scenario,
        "question": question,
        "category": "Scenario-based"
    }

# Generate scenario questions
scenario_questions = [create_scenario_question(s) for s in scenarios[:3]]
print("Sample Scenario Questions:")
for sq in scenario_questions:
    print(f"\n• {sq['question']}")