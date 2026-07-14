from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Test"

students = [
    {"name": "John Doe",    "score": 85},
    {"name": "Jane Smith",  "score": 92},
    {"name": "Bob Johnson", "score": 78},
    {"name": "Alice Lee",   "score": 61},
    {"name": "Charlie Wu",  "score": 45},
    {"name": "Diana Ross",  "score": 88},
]

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('test_template.html')

# Summary stats computed in Python (template-friendly)
scores = [s["score"] for s in students]
avg_score   = sum(scores) / len(scores)
high_score  = max(scores)
low_score   = min(scores)
pass_count  = sum(1 for s in scores if s >= 60)
pass_rate   = round(pass_count / len(scores) * 100, 1)

output = template.render(
    students=students,
    max_score=max_score,
    test_name=test_name,
    avg_score=avg_score,
    high_score=high_score,
    low_score=low_score,
    pass_rate=pass_rate,
)
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(output)
