from flask import Blueprint, render_template, send_file
blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def main_site():
  return render_template('simple_pages/index.html'),('main_site.html')

@blueprint.route('/myshoppinglist/')
def legal():
  return send_file('ingredients/my_shoppinglist.txt', as_attachment=True)
  

@blueprint.route('/ingredients/')
def ingredients():
  return render_template('simple_pages/ingredients.html')