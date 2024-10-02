from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory database (dictionary)
students = {}

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    name = request.form['name']
    if student_id and name:
        students[student_id] = {'name': name, 'attendance': []}
    return redirect(url_for('index'))

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    student_id = request.form['student_id']
    if student_id in students:
        date_today = datetime.today().strftime('%Y-%m-%d')
        students[student_id]['attendance'][date_today].append('Present')
    return redirect(url_for('index'))

@app.route('/attendance/<student_id>')
def attendance(student_id):
    student = students.get(student_id)
    return render_template('attendance.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

 
