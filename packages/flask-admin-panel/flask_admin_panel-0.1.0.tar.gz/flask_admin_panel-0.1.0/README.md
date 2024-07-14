# Flask-Admin-Panel
A [Flask][] extension that enables Admin Panel for Registed Flask-SQLAlchemy Models.

[Flask]: https://flask.palletsprojects.com

## Example

Setting up the Flask-Admin-Panel is simple:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin_panel import FlaskAdminPanel

app = Flask(__name__)
app.config["SECRET_KEY"] = "<replace with a secret key>"
app.config["APP_ADMIN_USER"] = "<replace with a your user name default is admin>"
app.config["APP_ADMIN_PASSWORD"] = "provide a strong password"
app.config["SQLALCHEMY_DATABASE_URI"] = "provide a sql alchemy database uri"

db = SQLAlchemy(app)

adminpanel = FlaskAdminPanel(app,db)
```

Registring the models to Flask-Admin-Panel :
```python

#Create any model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Provide unique name to model and SQLAlchemy.Model class
adminpanel.serv_admin_panel.register_model_for_admin_panel("User",User) 
```