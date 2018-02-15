# import necessary libraries
import os
import random
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///"
db = SQLAlchemy(app)


from .models import {{cookiecutter.model_name}}
#################################################
# Database Setup
#################################################

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()
    first = {{cookiecutter.model_name}}(name='test1')
    second = {{cookiecutter.model_name}}(name='test2')
    db.session.add(first)
    db.session.add(second)
    db.session.commit()


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    results = db.session.query({{cookiecutter.model_name}}.name).all()
    data = {
        "names": [result[0] for result in results],
        "heights": [random.randint(10, 100) for result in results]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()
