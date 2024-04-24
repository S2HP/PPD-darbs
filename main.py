from flask import Flask, render_template, request, session, redirect

app = Flask('app')
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/videodetail')
def videodetail():
    return render_template('video-detail.html')

@app.route('/photodetail')
def photodetail():
    return render_template('photo-detail.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

app.run(host='0.0.0.0', port=81)