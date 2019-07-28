#from mymodule import app
#from db_config import mysql
from flask import jsonify
from flask import flash, request
from flask_restful import Resource, Api, reqparse
# it convert password in hashcode md5 format
import hashlib
from werkzeug import generate_password_hash, check_password_hash 
import sqlite3
from flask import Flask, current_app
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
import tkinter as tk
from tkinter import *


def create_app():
    app = Flask(__name__)

    with app.app_context():
        print(current_app.name)


    return app

app = create_app()



api = Api(app)

#use for registering new user
class add_new_user(Resource):
    def post(self):
        try:
            username = request.form['username']
            password = request.form['password']
            hash_password = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
            conn = sqlite3.connect('networkusers.db')
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
            query = cursor.execute("SELECT * FROM member WHERE username = ?;",(username,))
            l = len(list(query))
            if l == 0: # user not present
                cursor.execute("INSERT INTO member (username, password) VALUES (?, ?);",(username, hash_password)) #,
                conn.commit()
                resp = jsonify("User added successfully!!")
                resp.status_code = 200
                return resp
            else:
                resp = jsonify("Registration failed!!")
                resp.status_code = 500
                return resp
        except Exception as e:
            resp = jsonify("Registration Failed!!")
            resp.status_code = 400
            return resp
        finally:
            cursor.close()
            conn.close()
                
#call by server for getting all users
class all_users(Resource):
    def get(self):
    	try:
    		conn = sqlite3.connect('networkusers.db')
    		cursor = conn.cursor()
    		cursor.execute("SELECT mem_id,username,password FROM member;")
    		rows = cursor.fetchall()
    		resp = jsonify(rows)
    		resp.status_code = 200
    		return resp
    	except Exception as e:
            resp = jsonify("Can't able to fetch data!!")
            resp.status_code = 400
            return resp
    	finally:
    		cursor.close() 
    		conn.close()
            
#use for client login
class one_user(Resource):
    def get(self):
        try:
            username = request.form['username']
            password = request.form['password']
            hash_password = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
            conn = sqlite3.connect('networkusers.db')
            cursor = conn.cursor()
            query = cursor.execute("SELECT username, password FROM member WHERE username = ? and password = ?;",(username, hash_password))
            l = len(list(query))
            if l > 0:
                row = query.fetchone()
                resp = jsonify(row)
                resp.status_code = 200
                #print(resp)
                return resp
            else:
                raise Exception("Not Logged In")
        except Exception as e:
            row = query.fetchone()
            resp = jsonify(row)
            resp.status_code = 400
            return resp
        finally:
            cursor.close()
            conn.close()
        
#forget password
class update_data(Resource):
    def put(self):
        try:
            conn = sqlite3.connect("networkusers.db")
            cursor = conn.cursor()
            username = request.form['username']
            password = request.form['password']
            hash_password = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
            cursor.execute("SELECT * FROM member WHERE username= ?;",(username,))
            query = cursor.execute("SELECT * FROM member WHERE username = ?;",(username,))
            l = len(list(query))
            
            if l > 0:
                cursor.execute("UPDATE member SET password = ? WHERE username= ?;", (hash_password,username,)) #,(hash_password, username)
                conn.commit()
                resp = jsonify("Password updated successfully!!")
                resp.status_code = 200
                return resp
            else:
                row = query.fetchone()
                resp = jsonify(row)
                resp.status_code = 400
                return resp
        except Exception as e:
            #row = query.fetchone()
            resp = jsonify("user not present")
            resp.status_code = 405
            return resp
        finally:
            cursor.close()
            conn.close()

#use for storing free port and ip address in port table
class update_port(Resource):
    def post(self):
        try:
            conn = sqlite3.connect("networkusers.db")
            cursor = conn.cursor()
            username = request.form['username']
            ip = request.form['ip']
            port1 = request.form['port1']
            port2 = request.form['port2']
            port3 = request.form['port3']
            cursor.execute("CREATE TABLE IF NOT EXISTS port (username TEXT, ip TEXT, port1 INTEGER, port2 INTEGER, port3 INTEGER, is_active INTEGER DEFAULT 0 NOT NULL);")
            query=cursor.execute("SELECT * FROM port WHERE port1= ? or port2=? or port3=?;",(port1,port2,port3))
            l = len(list(query))
            if l == 0:
                query2=cursor.execute("SELECT * FROM port WHERE username=?;",(username,))
                l2 = len(list(query2))
                if l2 != 0:
                    cursor.execute("UPDATE port SET ip=?, port1=?, port2=?, port3=? WHERE username=?;",(ip, port1, port2, port3, username))
                    conn.commit()
                else:
                    cursor.execute("INSERT INTO port (username,ip, port1, port2, port3) VALUES (?,?,?,?,?);", (username,ip,port1,port2,port3))
                    conn.commit()
                resp = jsonify("Port assigned successfully!!")
                resp.status_code = 200
                return resp
            else:
                row = query.fetchone()
                resp = jsonify(row)
                resp.status_code = 400
                return resp
        except Exception as e:
            resp = jsonify("Port Not assigned!!")
            resp.status_code = 405
            return resp
        finally:
            cursor.close()
            conn.close()
            
#fetch ip which are login
class get_login_ip(Resource):
    def get(self):
    	try:
    		conn = sqlite3.connect('networkusers.db')
    		cursor = conn.cursor()
    		cursor.execute("SELECT ip FROM port;")
    		rows = cursor.fetchall()
    		resp = jsonify(rows)
    		resp.status_code = 200
    		return resp
    	except Exception as e:
            resp = jsonify("Can't able to fetch data!!")
            resp.status_code = 400
            return resp
    	finally:
    		cursor.close() 
    		conn.close()
#check which user is login
class check_user_login(Resource):
    def post(self):
        try:
            conn = sqlite3.connect("networkusers.db")
            cursor = conn.cursor()
            username = request.form['username']
            cursor.execute("SELECT * FROM port WHERE username= ?;",(username,))
            query = cursor.execute("SELECT * FROM port WHERE username = ?;",(username,))
            l = len(list(query))
            
            if l > 0:
                cursor.execute("UPDATE port SET is_active = 1 WHERE username= ?;", (username,)) #,(hash_password, username)
                conn.commit()
                resp.status_code = 200
                return resp
            else:
                row = query.fetchone()
                resp = jsonify(row)
                resp.status_code = 400
                return resp
        except Exception as e:
            resp = jsonify("Can't able to fetch data!!")
            resp.status_code = 405
            return resp
        finally:
            cursor.close()
            conn.close()
            
#use for updating when user logout
class check_user_logout(Resource):
    def post(self):
        try:
            conn = sqlite3.connect("networkusers.db")
            cursor = conn.cursor()
            username = request.form['username']
            cursor.execute("SELECT * FROM port WHERE username= ?;",(username,))
            query = cursor.execute("SELECT * FROM port WHERE username = ?;",(username,))
            l = len(list(query))
            if l > 0:
                cursor.execute("UPDATE port SET is_active = 0 WHERE username= ?;", (username,)) #,(hash_password, username)
                conn.commit()
                resp.status_code = 200
                return resp
            else:
                row = query.fetchone()
                resp = jsonify(row)
                resp.status_code = 400
                return resp
        except Exception as e:
            resp = jsonify("Can't able to fetch data!!")
            resp.status_code = 405
            return resp
        finally:
            cursor.close()
            conn.close()
'''
class delete_data(Resource):
    def delete(self):
        try:
            conn = sqlite3.connect("networkusers.db")
            cursor = conn.cursor()
            username = request.form['username']
            cursor.execute("DELETE FROM port where username=?;",(username,))
            conn.commit()
            resp = jsonify('Port Dealocated successfully!!')
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
'''
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: '+request.url,
            }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


api.add_resource(add_new_user,'/post') #insert
api.add_resource(all_users, '/users') # display all users
api.add_resource(one_user, '/get') # display one user
api.add_resource(update_data, '/forget') #password update
#api.add_resource(delete_data, '/delete') #delete one entry
api.add_resource(update_port,'/port')
api.add_resource(check_user_login,'/user_activate')
api.add_resource(check_user_logout,'/user_deactivate')
api.add_resource(get_login_ip,'/get_login_ip')

if __name__ == "__main__":
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip =(s.getsockname()[0])
    s.close()
    ip = '192.168.43.64'
    app.run(host= ip, port=5111,debug=True)

