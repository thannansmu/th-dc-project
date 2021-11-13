from flask import Flask, render_template, redirect
import random
from truth_table import generate_url_id


app = Flask(__name__,template_folder = "Templates")


@app.route("/")
def main():
    return redirect("/truth_table_home")
    
@app.route("/truth_table_home")
def truth_table_home():
    return render_template("main_page.html")


@app.route("/truth_table=<id>")
def truth_table(id):
    return render_template("main_page.html")
    
    
@app.route("/create_table", methods=['POST', 'GET'])
def create_table():
    id = generate_url_id()
    return redirect("/truth_table=" + id)


@app.errorhandler(404)
def not_found(error):
    return redirect("/truth_table"), 404  



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
