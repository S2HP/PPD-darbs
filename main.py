from flask import Flask, render_template, request, session, redirect

app = Flask('app')
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("mainpage.html")
def index():
    return render_template('index.html')

@app.route('/basics')
def basics():
    return render_template('basics.html')

@app.route('/detailedInfo')
def detailedInfo():
    return render_template('detailedInfo.html')

app.run(host='0.0.0.0', port=81)