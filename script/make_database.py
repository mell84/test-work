#!/usr/bin/env  python3

# First program with flask
from flask import Flask
from subprocess import Popen
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    subprocess.call(['/app/1.py'], shell=True, stdout=subprocess.PIPE)
    return " Йоууу Мазафакер!!! Ты создал базу данных\n"


#@app.route("/x11vnc")
#def hello():
#    subprocess.call(['/etc/init.d/x11vnc'], shell=True, stdout=subprocess.PIPE)
#    return "X11vnc has been started. Site was wroute in the @flask@ \n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9002)

