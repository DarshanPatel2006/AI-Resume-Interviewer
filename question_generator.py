def generate_questions(skills):

    question_bank = {
        "Python": "Explain the difference between list and tuple in Python.",
        "Java": "What is the difference between JDK, JRE, and JVM?",
        "JavaScript": "Explain closures in JavaScript.",
        "React": "What is the Virtual DOM in React?",
        "Node.js": "What is event-driven architecture in Node.js?",
        "MongoDB": "What is indexing in MongoDB?",
        "SQL": "What is the difference between JOIN and UNION?",
        "Django": "What is Django ORM?",
        "Flask": "What is the difference between Flask and Django?",
        "Machine Learning": "What is overfitting in machine learning?",
        "Deep Learning": "What is the difference between CNN and RNN?"
    }

    questions = []

    # Intro question
    questions.append("Tell me about yourself.")

    # Skill-based questions
    for skill in skills:
        if skill in question_bank:
            questions.append(question_bank[skill])

    # Task question
    questions.append("Write a Python function to reverse a string.")

    return questions