from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dev'  # For demo only — use an environment variable in production

tarefas = []

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefa = request.form.get('tarefa')
    if tarefa:
        tarefas.append(tarefa)
        flash('Tarefa adicionada.')
    return redirect(url_for('index'))

@app.route('/remover/<int:index>', methods=['POST'])
def remover(index):
    if 0 <= index < len(tarefas):
        tarefas.pop(index)
        flash('Tarefa removida.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)