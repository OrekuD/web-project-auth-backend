from flask import Flask, jsonify
from flask_cors import CORS
from user.models import User

app = Flask(__name__)
CORS(app)

api_version = "/api/v1"

@app.route('/')
def home():
    return jsonify({"msg": "home"})
  
@app.route(api_version + '/user/sign-up', methods=['POST'])
def signup():
  return User().signUp()

@app.route(api_version + '/user/sign-out', methods=['GET'])
def signout():
  return User().signOut()

@app.route(api_version + '/user/update', methods=['PUT'])
def update():
  return User().updateDetails()

@app.route(api_version + '/user/sign-in', methods=['POST'])
def login():
  return User().signIn()

if __name__ == "__main__":
  app.run(host='localhost', port=5000)

 