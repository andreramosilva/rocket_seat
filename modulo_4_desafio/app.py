from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from refeicao import Refeicao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/refeicoes', methods=['POST'])
def create_refeicao():
    data = request.get_json()

    refeicao = Refeicao(nome=data['nome'], descricao=data['descricao'])
    db.session.add(refeicao)
    db.session.commit()

    return jsonify({'id': refeicao.id})

@app.route('/refeicoes', methods=['GET'])
def get_refeicoes():
    refeicoes = Refeicao.query.all()

    return jsonify([refeicao.__dict__ for refeicao in refeicoes])

@app.route('/refeicoes/<int:id>', methods=['GET'])
def get_refeicao(id):
    refeicao = Refeicao.query.get(id)

    return jsonify(refeicao.__dict__)

@app.route('/refeicoes/<int:id>', methods=['PUT'])
def update_refeicao(id):
    data = request.get_json()

    refeicao = Refeicao.query.get(id)
    refeicao.nome = data['nome']
    refeicao.descricao = data['descricao']
    db.session.commit()

    return jsonify(refeicao.__dict__)

@app.route('/refeicoes/<int:id>', methods=['DELETE'])
def delete_refeicao(id):
    refeicao = Refeicao.query.get(id)
    db.session.delete(refeicao)
    db.session.commit()

    return jsonify(refeicao.__dict__)


if __name__ == '__main__':
    app.run(debug=True)