import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillproof.settings')
django.setup()

from core.models import Skill, Test, User

def seed():
    # Create Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser created: admin / admin123")

    # Create Skills
    python, _ = Skill.objects.get_or_create(
        name="Python Programming",
        description="Test your knowledge of Python basics, data structures, and object-oriented programming.",
        category="Programming"
    )
    
    react, _ = Skill.objects.get_or_create(
        name="React.js",
        description="Validate your skills in building modern UIs with React, Hooks, and State Management.",
        category="Frontend"
    )

    # Create Tests for Python
    Test.objects.get_or_create(
        skill=python,
        question="What is the output of print(type([]) == list)?",
        option_a="True",
        option_b="False",
        option_c="Error",
        option_d="None",
        correct_answer="A"
    )
    Test.objects.get_or_create(
        skill=python,
        question="Which keyword is used to define a function in Python?",
        option_a="func",
        option_b="define",
        option_c="def",
        option_d="fn",
        correct_answer="C"
    )

    # Create Tests for React
    Test.objects.get_or_create(
        skill=react,
        question="Which hook is used to manage state in a React functional component?",
        option_a="useEffect",
        option_b="useState",
        option_c="useContext",
        option_d="useReducer",
        correct_answer="B"
    )

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
