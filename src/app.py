from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_new_todo():
    # request_body = request.get_json()
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    
    # print(request_body)
    print(todos)
    print("incoming resuqet wuth the body", request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if len(todos) == 0:
        return 'No more task to delete'
    if position >= len(todos):
        return 'No task found'
    todos.pop(position)
    print('this is the positio ton delete', position)
    return jsonify(todos), 200




# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__': # nombre interno 
  app.run(host='0.0.0.0', port=3245, debug=True)