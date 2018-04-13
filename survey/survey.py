from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'x'
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def render_result():
    name = request.form['name']
    lang = request.form['lang']
    loca = request.form['loca']
    comm = request.form['comm']
    if len(comm) < 1:
        flash("Name cannot be empty!")
    elif len(comm) > 120:
        flash("Name cannot exceed 120 chars!")
    else:
        flash("Success! Your comment has been submitted")
    if len(name) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(name)
    return render_template('result.html', name=name, lang=lang, loca=loca, comm=comm)
app.run(debug=True)
