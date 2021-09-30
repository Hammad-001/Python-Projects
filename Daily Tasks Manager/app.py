# imports flask, database .datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# start flask app
app = Flask(__name__)
# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# assigning database to db
db = SQLAlchemy(app)


class ToDo(db.Model):
    # id of task
    id = db.Column(db.Integer, primary_key=True)
    # task content
    task_content = db.Column(db.String(200), nullable=False)
    # creation date
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    # represent To Do object in string 
    def __repr__(self):
        return "<Task %r>" % self.id


# when user is on index.html both get/post methods
@app.route("/", methods=["GET", "POST"])
# function ran to show index.html
def index():
    # check if request is post or get
    if request.method == "POST":
        # getting content from page
        task_content =  request.form["content"]
        # creating new object of To Do
        add_task = ToDo(task_content=task_content)
        # try insertion in database
        try:
            #add object to database
            db.session.add(add_task)
            # commiting changes in database
            db.session.commit()
            # again redirect to index.html
            return redirect("/")
        except:
            # if any exception happens
            return "There was an issue in adding your task!"
    else:
        # if request is get then sort To Do objects on basis of creation date
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        # then render index.html and pass tasks as argument
        return render_template("index.html", tasks=tasks)

# when user click on delete button
# it gets task id in page url
@app.route('/delete/<int:id>')
#this function ran on press of delete
def delete(id):
    # first search task on base id in To Do objects 
    task_to_be_deleted = ToDo.query.get_or_404(id)
    # try to delete from database
    try:
        # try to delete selected object
        db.session.delete(task_to_be_deleted)
        # commmiting changes to database
        db.session.commit()
        #again redirect to index.html
        return redirect("/")
    except:
        # if cannot delete from database, show error
        return "There is a problem in deleting that Task!"

# when user click on update task
# it both has methods get and post + it contains id in page url
@app.route('/update/<int:id>', methods=["GET", "POST"])
# it ran on clicking on update task
def update(id):
    # select task from To Do objects
    task_to_be_updated = ToDo.query.get_or_404(id)
    # if request is post
    if request.method == "POST":
        # simply assign the task new value from page
        task_to_be_updated.task_content =  request.form["content"]        
        #try to commit changes in database
        try:
            # try to commit changes
            db.session.commit()
            # redirect to index.html
            return redirect("/")
        except:
            # if cannot update show error
            return "There was an issue in updating your task!"
    else:
        # if request is get then pass selected task to update.html
        return render_template("update.html", task=task_to_be_updated)
    
    # if file is ran on by its own
if __name__ == "__main__":
    # debug=True to show error while development
    app.run(debug=False)