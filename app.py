from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    competed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "<Task  %r>" % self.id


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        if len(task_content) > 0:
            new_task = Todo(content=task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect("/")
            except:
                return "there is issue to  the server"
        else:
            return redirect("/")

    else:
        tasks = Todo.query.all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task_del = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_del)
        db.session.commit()
        return redirect("/")
    except:
        return "there is problem with delete that task"


@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "there is problem with server"
    else:
        return render_template("update.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
