from flask import jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid
from resources.errorResource import ErrorResource
from resources.okayResource import OkayResource
from resources.userResource import UserResource
from db import db
class User:
  def signOut(self):
    # destroy accesstoken
    return jsonify(OkayResource().getResource("success")), 200

  def signUp(self):
    if db.users.find_one({ "email": request.json['email'].lower() }):
      return jsonify(ErrorResource().getResource(400, "Email address already exist")), 400

    new_user = {
      "_id": uuid.uuid4().hex,
      "email": request.json['email'].lower(),
      "firstName": request.json['firstName'],
      "lastName": request.json['lastName'],
      "password": pbkdf2_sha256.encrypt(request.json['password'])
    }
    
    created_user = db.users.insert_one(new_user)
    
    if created_user:
      return jsonify(UserResource().getResource(new_user)), 200
    
    return jsonify(ErrorResource().getResource(500, "User creation failed")), 500
  
  def updateDetails(self):
    found_user = db.users.find_one({ "_id": request.json['_id'] })
    if not found_user:
      return jsonify(ErrorResource().getResource(404, "User doesn't exist")), 404
    
    user = {}
    
    if found_user['email'] == request.json['email'].lower():
      user = {
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
      }

    else:
      if db.users.find_one({ "email": request.json['email'].lower() }):
        return jsonify(ErrorResource().getResource(400, "Email address already exist")), 400
      
      user = {
        "email": request.json['email'].lower(),
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
      }
    
    updated_user = db.users.update_one({"_id": request.json['_id']}, {'$set': user})
    
    if updated_user:
      return jsonify(OkayResource().getResource("success")), 200
    
    return jsonify(ErrorResource().getResource(500, "User update failed")), 500
  
  def changePassword(self):
    user = db.users.find_one({ "_id": request.json['_id'] })
    if not user:
      return jsonify(ErrorResource().getResource(404, "User doesn't exist")), 404
    
    payload = {
      'password': pbkdf2_sha256.encrypt(request.json['newPassword'])
    }
    
    if pbkdf2_sha256.verify(request.json['oldPassword'], user['password']):
      updated_user = db.users.update_one({"_id": request.json['_id']}, {'$set': payload })
      if updated_user:
        return jsonify(OkayResource().getResource("success")), 200
    
    return jsonify(ErrorResource().getResource(500, "Password change failed")), 400
    
  
  def signIn(self):
    user = db.users.find_one({
      "email": request.json['email'].lower()
    })
    
    if not user:
      return jsonify(ErrorResource().getResource(401, "User not found")), 401
    
    if pbkdf2_sha256.verify(request.json['password'], user['password']):
      return jsonify(UserResource().getResource(user)), 200
    
    return jsonify(ErrorResource().getResource(401, "Invalid credentials")), 401
    