from flask import Blueprint, Flask, jsonify, redirect,render_template, request,flash, send_file , url_for,session,render_template_string

app = Flask(__name__,template_folder='templates', static_folder='static')

@app.route("/")
def welcome():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True, host='localhost', port=5)
    # app.run(debug=True)