######################################################################
# Project           : JSONP Attack
#
# Program name      : mitigated.py
#
# Author            : Evan Kivolowitz
#
# Date created      : 02/19/2019
#
# Purpose           : Proxy server to restructure application.
#
# Credit            : 
#
# Use                                    Source
#
# Revision History  :
#
# Date        Author              Ref    Revision 
# 02/19/2019  Evan Kivolowitz      1     Created prototype of project.
#
######################################################################
from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def run():
	# put your code here to request data and send data to the front end
	return "So long, and thanks for all the fish."
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
