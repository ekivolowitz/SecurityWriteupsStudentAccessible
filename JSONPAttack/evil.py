######################################################################
# Project           : JSONP Attack
#
# Program name      : evil.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 02/19/2019
#
# Purpose           : Attack server to JSONP.  
#
# Credit            :
#
# Use                                    Source
#
# Revision History  :
#
# Date        Author              Ref    Revision 
# 02/19/2019  Evan Kivolowitz      1     Created prototype of project.
# 02/28/2019  Evan Kivolowitz      2     Updated headers.
#
######################################################################
from flask import Flask, request, render_template, jsonify
from pprint import pprint
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/content", methods=["POST", "GET"])
def run():
    # Fill out this method to accept posts requests.
    # Simply print the body data to show you have successfully 
    # stolen it.
    return "Thank you for the data!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
