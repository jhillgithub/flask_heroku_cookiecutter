from .app import db

class {{cookiecutter.model_name}}(db.Model):
    __tablename__ = '{{cookiecutter.table_name}}'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '<{{cookiecutter.model_name}} %r>' % (self.name)
