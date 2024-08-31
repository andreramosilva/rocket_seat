from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
# view login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    senha = data.get('senha')

    if username and senha:
        user = User.query.filter_by(username=username).first()

        if user is not None and user.senha == senha:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message': 'User authenticated'})
    
    return jsonify({'message': 'User not authenticated'}), 401

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'User logged out'})

@app.route('/user', methods=['POST'])
@login_required
def create_user():
    data = request.json
    username = data.get('username')
    senha = data.get('senha')

    if username and senha:
        user = User(username=username, senha=senha)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created'})

    return jsonify({'message': 'User not created'}), 400

@app.route('/user/<int:id>', methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get(id)

    if user:
        return jsonify({'id': user.id, 'username': user.username, 'senha': user.senha})

    return jsonify({'message': 'User not found'}), 404

@app.route('/user/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)

    if user and id == current_user.id:
        data = request.json
        user.username = data.get('username', user.username)
        user.senha = data.get('senha', user.senha)
        db.session.commit()
        return jsonify({'message': 'User updated'})

    return jsonify({'message': 'User not found'}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user= User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'}), 404







@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)