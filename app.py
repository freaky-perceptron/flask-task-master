from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class TaskMaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
  
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = TaskMaster(task = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'That didnt work'
    else:
        Tasks = TaskMaster.query.order_by(TaskMaster.id).all()
        return render_template('home.html', tasks=Tasks)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    del_task = TaskMaster.query.get(id)
        
    try:
        db.session.delete(del_task) 
        db.session.commit()
        return redirect('/') 
    except:
        return 'That didnt work'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == "GET":
        Task = TaskMaster.query.get(id)
        return render_template('update.html', Task=Task)
    else:
        updated_task = request.form['updated']
        TaskMaster.query.get(id).task = updated_task

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'That didnt work'

if __name__ == "__main__":
    app.run(debug=True)
