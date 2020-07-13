import time
import os
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName != 'monstermash':
        if deviceName == 'lock':
            os.system('./parentlock.sh')
        if deviceName == 'unlock':
            os.system('./parentunlock.sh')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

