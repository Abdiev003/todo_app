from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import collections
import json


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean)

    def __init__(self, title, completed):
        self.title = title
        self.completed = completed


class TodoSerializer:
    def __init__(self, todo):
        self.todo = todo

    def toDict(self):
        return collections.OrderedDict([
            ('id', self.todo.id),
            ('title', self.todo.title),
            ('completed', self.todo.completed),
        ])


@app.route('/api/v1/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        todo_data = Todo.query.all()
        serialized_data = [TodoSerializer(todo).toDict() for todo in todo_data]
        return jsonify(serialized_data)
    else:
        title = request.json['title']
        completed = False
        todo = Todo(title, completed)
        db.session.add(todo)
        db.session.commit()
        return jsonify({
            'success': 'success'
        })


@app.route('/add', methods=['GET', 'POST'])
def addTodos():
    if request.method == 'GET':
        return render_template('add-todo.html')
    else:
        title = request.json['title']
        completed = False
        todo = Todo(title, completed)
        db.session.add(todo)
        db.session.commit()
        return jsonify({
            'success': 'success'
        })


@app.route('/api/v1/todos', methods=['GET', 'DELETE'])
def deleteTodos():
    if request.method == 'GET':
        todo_data = Todo.query.all()
        serialized_data = [TodoSerializer(todo).toDict() for todo in todo_data]
        return jsonify(serialized_data)
    elif request.method == 'DELETE':
        id_data = request.json['id']
        todo = Todo.query.get(id_data)
        db.session.delete(todo)
        db.session.commit()
        todo_data = Todo.query.all()
        serialized_data = [TodoSerializer(todo).toDict() for todo in todo_data]
        return jsonify(serialized_data)

@app.route('/api/v1/todos', methods=['GET', 'PUT'])
def putTodos():
    if request.method == 'GET':
        todo_data = Todo.query.all()
        serialized_data = [TodoSerializer(todo).toDict() for todo in todo_data]
        return jsonify(serialized_data)
    elif request.method == 'PUT':
        id_data = request.json['id']
        todo = Todo.query.get(id_data)
        if todo.completed == True:
            todo.completed = False
        else:
            todo.completed = True
        
        db.session.add(todo)
        db.session.commit()

        serialized_data = TodoSerializer(todo).toDict()
        return jsonify(serialized_data)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
