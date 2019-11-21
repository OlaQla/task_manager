import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
#app.config["MONGO_DBNAME"] = 'task_manager'
MONGODB_URI = "mongodb+srv://ola:Ola123@myfirstcluster-wl3fx.mongodb.net/task_manager"
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route('/add_task')
def add_task():
    return render_template('addtask.html')

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)