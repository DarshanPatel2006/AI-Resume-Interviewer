def extract_skills(resume_text):

    skills_db = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB",
        "SQL",
        "Django",
        "Flask",
        "HTML",
        "CSS",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Pandas",
        "NumPy"
    ]

    detected_skills = []

    for skill in skills_db:
        if skill.lower() in resume_text.lower():
            detected_skills.append(skill)

    return detected_skills