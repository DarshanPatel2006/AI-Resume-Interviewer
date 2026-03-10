from flask import Flask, render_template, request
from resume_loader import load_resume
from skill_extractor import extract_skills
from question_generator import generate_questions
from answer_evaluator import evaluate_answers
import os

app = Flask(__name__)

UPLOAD_FOLDER = "data"


@app.route("/", methods=["GET", "POST"])
def upload_resume():

    if request.method == "POST":

        file = request.files["resume"]

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        resume_text = load_resume(file_path)

        skills = extract_skills(resume_text)

        

        if len(skills) < 5:
            return render_template(
                "upload.html",
                error="This resume is not suitable. Please upload a resume with at least 5 technical skills."
            )
        questions = generate_questions(skills)

        return render_template("interview.html", questions=questions)

    return render_template("upload.html")


@app.route("/submit", methods=["POST"])
def submit_answers():

    answers = []

    for key in request.form:
        answers.append({
            "question": key,
            "answer": request.form[key]
        })

    report = evaluate_answers(answers)

    return render_template("report.html", report=report)


if __name__ == "__main__":
    app.run(debug=True)