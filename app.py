from flask import Flask, redirect, url_for, render_template, send_file
app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def main_site():
  return render_template('main_site.html')

@app.route('/myshoppinglist/')
def legal():
  return send_file('ingredients/my_shoppinglist.txt', as_attachment=True)
  

@app.route('/ingredients/')
def ingredients():
  return render_template('ingredients.html')

if __name__ == '__main__':
  app.run()