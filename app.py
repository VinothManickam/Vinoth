from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

todos = []

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """
    Get all todos
    ---
    responses:
      200:
        description: A list of todos
        schema:
          type: object
          properties:
            todos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  title:
                    type: string
    """
    return jsonify({'todos': todos})

@app.route('/api/todos', methods=['POST'])
def create_todo():
    """
    Create a new todo
    ---
    parameters:
      - name: todo
        in: body
        type: object
        required: true
        schema:
          type: object
          properties:
            todo:
              type: string
    responses:
      201:
        description: Created todo
        schema:
          type: object
          properties:
            todo:
              type: object
              properties:
                id:
                  type: integer
                title:
                  type: string
      400:
        description: Invalid request
        schema:
          type: object
          properties:
            error:
              type: string
    """
    todo = request.get_json().get('todo')
    if todo:
        new_todo = {'id': len(todos) + 1, 'title': todo}
        todos.append(new_todo)
        return jsonify({'todo': new_todo}), 201
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
