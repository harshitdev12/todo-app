from xxlimited import new

from flask import Flask,  jsonify, request, render_template,redirect
import os 
import json
from datetime import datetime

app = Flask(__name__)

TODOS_FILE = 'todos.json'

def load_todos():
    try:
        with open(TODOS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_todos(todos):
    with open(TODOS_FILE, 'w') as file:
        json.dump(todos, file, indent=4)


    
  
@app.route('/')
def index():
    return render_template('index.html', todos=load_todos(), total=len(load_todos()))



@app.route('/add', methods=['POST'])
def add_todo():
    data = request.get_json()
    print(data)
    title = data.get('title','').strip()

    if title:
        todos = load_todos()
        new_todo = {
            'id': len(todos) + 1,
            'title': title,
            'completed': False}
        todos.append(new_todo)
        save_todos(todos)
        return jsonify({'message': 'Todo added successfully', 'todos': todos}), 201
    else:
        return jsonify({'error': 'Title cannot be empty'}), 400 
   


@app.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    return jsonify({'message': 'Todo deleted successfully', 'todos': todos}), 200

@app.route('/toggle/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    save_todos(todos)
    return jsonify({'message': 'Todo toggled successfully', 'todos': todos}), 200   

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = load_todos()
    return jsonify({'todos': todos}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)