from flask import Flask, render_template, redirect, request
import random
from truth_table import generate_url_id, assign_truth_values

app = Flask(__name__,template_folder = "Templates")

#redirects to main page
@app.route("/")
def main():
    return redirect("/truth_table_home")
    
#main page
@app.route("/truth_table_home")
def truth_table_home():
    return render_template("main_page.html")

#page for truth table
@app.route("/truth_table=<id>")
def truth_table(id):
    return render_template("table.html")
    
#page that calls functions to create truth table
@app.route("/create_table", methods=['POST', 'GET'])
def create_table():
    id = generate_url_id()
    assign_truth_values(request.form["formula"])
    return redirect("/truth_table=" + id)

#404 error handler
@app.errorhandler(404)
def not_found(error):
    return redirect("/truth_table"), 404  

#Internal server error handler
@app.errorhandler(500)
def internal(error):
    return render_template("500.html")


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
