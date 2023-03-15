#!/usr/bin/env python3
"""
entry point for this application
"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)