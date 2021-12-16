from flask import Flask, request, jsonify
from models import Schema
from todoService import TodoService


app = Flask(__name__) #__main__

@app.route("/todo",methods = ["POST"])
def create_todo():
    req = request.get_json()
    print(req)
    return TodoService().create(req)

@app.route("/todo", methods = ["GET"])
def get_todos():
    return  jsonify(TodoService().get_all())


if __name__ == "__main__":
    Schema()
    app.run(debug = True)