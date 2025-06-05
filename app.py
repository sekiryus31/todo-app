from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []  # タスクを保存するリスト（メモリ上）
id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global id
    if request.method == 'POST':
        title = request.form.get('task')
        if title:
            tasks.append({'id':id, 'title':title})
            id += 1
        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks)


@app.route('/edit/<int:task_id>')
def edit(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    return render_template('edit.html', task=task)

@app.route('/edit/<int:task_id>', methods=['POST'])
def update(task_id):
    new_title = request.form.get('title')
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = new_title
            break
    return redirect('/')


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    global tasks
    new_tasks = []
    for task in tasks:
        if task[('id')] != task_id:
            new_tasks.append(task)
    tasks = new_tasks

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)