from flask import Flask, render_template, redirect
import random
from truth_table import create_table


app = Flask(__name__,template_folder = "Templates")


@app.route("/")
def main():
    return redirect("/truth_table")


@app.route("/truth_table")
def truth_table():
    return render_template("main_page.html")
    
    
@app.route("/create_table=<id>", methods=['POST', 'GET'])
def create_table(id):
    id = create_table();
    return render_template("table.html")


@app.errorhandler(404)
def not_found(error):
    return redirect("/truth_table"), 404  


















if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
