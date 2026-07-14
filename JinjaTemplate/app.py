from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name  = "python test"

students = [{"name": "John Doe", "score": 85},
            {"name": "Jane Smith", "score": 92},
            {"name": "Bob Johnson", "score": 78}]

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('test_template.html')

for student in students:
    student['percentage'] = (student['score'] / max_score) * 100
    student['grade'] = 'A' if student['percentage'] >= 90 else 'B' if student['percentage'] >= 80 else 'C' if student['percentage'] >= 70 else 'D' if student['percentage'] >= 60 else 'F'

output = template.render(students=students, max_score=max_score, test_name=test_name)
with open('output.html', 'w') as f:
    f.write(output)
