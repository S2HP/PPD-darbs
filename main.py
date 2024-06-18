from flask import Flask, render_template, request, session, redirect

app = Flask('app')
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/information')
def information():
    return render_template("information.html")

@app.route('/videodetail')
def videodetail():
    return render_template("video-detail.html")

@app.route('/photodetail/<picid>')
def photodetail(picid):
    return render_template("photo-detail.html",picid=picid)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/photodetail2')
def photodetail2():
    return render_template("photo-detail copy 1.html")

@app.route('/photodetail3')
def photodetail3():
    return render_template("photo-detail copy 2.html")
    
@app.route('/photodetail4')
def photodetail4():
    return render_template("photo-detail copy 3.html")

@app.route('/photodetail5')
def photodetail5():
    return render_template("photo-detail copy 4.html")

@app.route('/photodetail6')
def photodetail6():
    return render_template("photo-detail copy 5.html")

@app.route('/photodetail7')
def photodetail7():
    return render_template("photo-detail copy 6.html")

@app.route('/photodetail8')
def photodetail8():
    return render_template("photo-detail copy 7.html")

@app.route('/photodetail9')
def photodetail9():
    return render_template("photo-detail copy 8.html")

@app.route('/photodetail10')
def photodetail10():
    return render_template("photo-detail copy 9.html")

@app.route('/photodetail11')
def photodetail11():
    return render_template("photo-detail copy 10.html")

@app.route('/photodetail12')
def photodetail12():
    return render_template("photo-detail copy 11.html")

@app.route('/photodetail13')
def photodetail13():
    return render_template("photo-detail copy 12.html")

@app.route('/photodetail14')
def photodetail14():
    return render_template("photo-detail copy 13.html")

@app.route('/photodetail15')
def photodetail15():
    return render_template("photo-detail copy 14.html")

@app.route('/photodetail16')
def photodetail16():
    return render_template("photo-detail copy 15.html")


app.run(host='0.0.0.0', port=81)