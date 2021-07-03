![Flask: 2.0.1](https://img.shields.io/badge/Flask-2.0.01-yellowgreen)

# flask-task-master
This repository contains a code for CRUD app named **Task Master** in Flask

<center><img src="https://github.com/freaky-perceptron/flask-task-master/blob/master/Screenshot%20from%202021-07-03%2017-59-18.png" alt="screenshot" width=850 height=800></center>

### Functionalities
* Can add a task
* Can update a task
* Can delete a task
* Responsive

### How to use?
* Clone the repo
  ```bash
  git clone freaky-perceptron/flask-task-master
  ```
  
* Change the current directory to ```flask-task-master```
  ```bash
  cd flask-task-master
  ```
 
* Install the depencies
  ```bash
  pip3 install requirements.txt
  ```
 
* Open a python shell in the same repository and activate the databaase
  ```python
  >>from app import db
  >>db.create_all()
  >>exit()
  ```

* Now, run the task-master app on localhost server
  ```bash
  python3 app.py
  ```
  
 The flask-task-master can be seen running on [localhost](http://127.0.0.1:5000/) server
 
 
  



