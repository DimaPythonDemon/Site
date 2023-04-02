from flask import Flask, render_template, request, session
from functions import *

app = Flask(__name__)
app.secret_key = 'SuperSecretKeyX'


@app.route('/')
def start() -> 'html':
    return render_template("MainPage.html")

@app.route('/buxty')
def Buxty() -> 'html':
    return render_template("Buxty.html", data=get_data())

@app.route('/<Index>')
def Show_buxta(Index: str):
    session['WTF'] = Index
    return render_template("ShowBay.html", data=get_data(indx=int(session['WTF']))) if session['WTF'] != 'favicon.ico' else session['WTF']

@app.route('/how')
def Show_how():
    return render_template("How.html")

'''@app.route('/search4', methods=["POST", "GET"])
def do_search() -> 'html':
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    return render_template("results.html", the_title="AquaSev", the_phrase=phrase, the_letters=letters, the_results="ebanulsya")

@app.route('/entry', methods=["POST", "GET"])
def entry_page() -> 'html':
    return render_template("entry.html", the_title="AquaSev")
'''
app.run(port=4000, debug=True)