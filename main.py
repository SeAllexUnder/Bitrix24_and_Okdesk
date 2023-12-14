from flask import Flask, render_template
from flask import request
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hook_from_b24():
    with open('wh_saver.txt', 'a') as f:
        f.write(f"{datetime.now()} {request}\r")
    return "Outhookfromb24"


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5432, host='0.0.0.0')


