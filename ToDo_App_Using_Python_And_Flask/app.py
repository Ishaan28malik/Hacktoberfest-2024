# Hosted on : https://todo-vikrantshah.herokuapp.com/

from flask import Flask, render_template, request, redirect
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class ToDo(db.Model) :
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST" :
        title = request.form["title"]
        desc = request.form["desc"]

        todo = ToDo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()

    all_todos = ToDo.query.all()
    #print(all_todos)
    return render_template("index.html", all_todos = all_todos)

@app.route("/update/<int:sno>", methods = ["GET", "POST"])
def update(sno):
    if request.method == "POST" :
        title = request.form["title"]
        desc = request.form["desc"]

        todo = ToDo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
    
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
        
    todo = ToDo.query.filter_by(sno = sno).first()
    return render_template("update.html", todo = todo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = ToDo.query.filter_by(sno = sno).first()

    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__" :
    app.run(debug = True, port = 8000)