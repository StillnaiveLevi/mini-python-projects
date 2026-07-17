from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True  # auto-reload templates on change

MAX_SCORE = 100
TEST_NAME = "Python Test"

# In-memory student list — persists while the server is running
students = [
    {"name": "John Doe",    "score": 85},
    {"name": "Jane Smith",  "score": 92},
    {"name": "Bob Johnson", "score": 78},
    {"name": "Alice Lee",   "score": 61},
    {"name": "Charlie Wu",  "score": 45},
    {"name": "Diana Ross",  "score": 88},
]


def compute_stats():
    scores     = [s["score"] for s in students]
    avg_score  = sum(scores) / len(scores)
    high_score = max(scores)
    low_score  = min(scores)
    pass_count = sum(1 for s in scores if s >= 60)
    pass_rate  = round(pass_count / len(scores) * 100, 1)
    return avg_score, high_score, low_score, pass_rate


@app.route("/")
def index():
    avg_score, high_score, low_score, pass_rate = compute_stats()
    return render_template(
        "test_template.html",
        students=students,
        max_score=MAX_SCORE,
        test_name=TEST_NAME,
        avg_score=avg_score,
        high_score=high_score,
        low_score=low_score,
        pass_rate=pass_rate,
        form_action=url_for("add_student"),
    )


@app.route("/add", methods=["POST"])
def add_student():
    name  = request.form.get("name", "").strip()
    score_str = request.form.get("score", "").strip()

    if name and score_str.isdigit():
        score = int(score_str)
        if 0 <= score <= MAX_SCORE:
            students.append({"name": name, "score": score})

    return redirect(url_for("index"))


if __name__ == "__main__":
    print("Running at http://127.0.0.1:5000")
    app.run(debug=True)
