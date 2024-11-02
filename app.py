from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from e_com_boat.retrival_gen import generation
from e_com_boat.data_ingensation import data_ingensation

app = Flask(__name__)

load_dotenv()

vstore=data_ingensation("done")
chain=generation(vstore)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000)