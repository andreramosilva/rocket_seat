from flask import Flask, request, jsonify
from models.task import Task

# __name__ == __main__
tasks = []
task_id_control = 1
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "hello"

@app.route("/tasks",methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data.get("title"),description=data.get("description", ""))
    task_id_control+=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem" : "Nova tarefa criada com sucesso"}) 

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    # for task in tasks:
    #     task_list.append(task.to_dict())

    result = { "tasks": task_list,
              "total_tasks": len(task_list)
    }    
    return jsonify(result) 

@app.route("/tasks/<int>:id",methods=["GET"])
def get_task(id):
    task=None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message":"Nao foi possivel encontrar a atividade"}),404

@app.route("/tasks/<int:id>",methods=["PUT"])
def update_task(id):
    task = None
    
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({"message":"Nao foi possivel encontrar"}),404 
    
    data = request.get_json()    
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]

    return jsonify({"message":"Atualizaçao realizada com sucesso"})
if __name__ == "__main__":
    app.run(debug=True)