#!/usr/bin/python3
""" This is an example of flask jsonify """
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False,
        'zebra': 'An animal',
        'AirBnB': "clone Version 3"
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Testing what I learn to prepare for the AirBnB',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """ converts the dict to json """
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """gets task by id"""
    task = [tsk for tsk in tasks if tsk['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
