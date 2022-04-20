from . import routes, models
from app.extensions.database import db

class Recipes(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  working_steps = db.Column(db.String(2000))


class Ingredients(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  price = db.Column(db.Numeric(10, 2))
  type = db.Column(db.String(80))
  in_stock = db.Column(db.String(80))

