#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from libby.remote import udpRemote

app = Flask(__name__)
Bootstrap(app)


@app.route('/garage')
def garage():
    return render_template('index.html')

@app.route('/ampi')
def ampi():
    return render_template('ampi.html')
    

@app.route('/')
def index():
    nachricht = "Hallo Welt!"
    return render_template('index.html', nachricht=nachricht)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
