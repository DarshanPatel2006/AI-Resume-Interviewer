def evaluate_answers(answers):

    answered = 0
    skipped = 0
    weak = 0

    for item in answers:

        answer = item["answer"].strip().lower()

        # user says "i don't know"
        if answer in ["i don't know", "idk", "dont know"]:
            skipped += 1

        # empty answer
        elif answer == "":
            skipped += 1

        # weak answer
        elif len(answer) < 25:
            weak += 1
            answered += 1

        else:
            answered += 1

    total = len(answers)

    if total == 0:
        score = 0
    else:
        score = int((answered - weak) / total * 10)

    progress = score * 10

    if score < 4:
        level = "Beginner"
        advice = "Your answers show limited understanding of the topics. Focus on strengthening fundamental concepts and practicing technical questions."

    elif score < 7:
        level = "Intermediate"
        advice = "You have a good base, but some answers lacked depth. Practice explaining concepts clearly and solving more interview problems."

    else:
        level = "Strong Candidate"
        advice = "Great job! Your responses demonstrate strong understanding. Continue practicing advanced problems and real-world scenarios."

    return {
        "answered": answered,
        "skipped": skipped,
        "weak": weak,
        "score": score,
        "progress": progress,
        "level": level,
        "advice": advice
    }