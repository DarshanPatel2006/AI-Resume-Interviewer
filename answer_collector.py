def collect_answers(questions):

    answers = []

    for i, question in enumerate(questions, 1):

        print(f"\nQuestion {i}: {question}")

        print("Type your answer below. Type 'done' when finished or 'skip' to skip.\n")

        user_lines = []

        while True:
            line = input()

            if line.lower() == "done":
                break

            if line.lower() == "skip":
                user_lines = ["skip"]
                break

            user_lines.append(line)

        answer = "\n".join(user_lines)

        answers.append({
            "question": question,
            "answer": answer
        })

    return answers
