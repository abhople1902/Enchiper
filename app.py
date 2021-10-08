from flask import Flask, request, jsonify, render_template, redirect


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index copy.html')





if __name__ == "__main__":
    app.run(debug=True)
