from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Task %r>" % self.id



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content =  request.form["content"]
        
        add_task = ToDo(task_content=task_content)
        
        try:
            db.session.add(add_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue in adding your task!"
    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        return render_template("index.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_be_deleted = ToDo.query.get_or_404(id)
      
    try:
        db.session.delete(task_to_be_deleted)
        db.session.commit()
        return redirect("/")
    except:
        return "There is a problem in deleting that Task!"


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    task_to_be_updated = ToDo.query.get_or_404(id)
    
    if request.method == "POST":
        task_to_be_updated.task_content =  request.form["content"]        
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue in updating your task!"
    else:
        return render_template("update.html", task=task_to_be_updated)
    

if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
    
    
if __name__ == "__main__":
    app.run(debug=True)