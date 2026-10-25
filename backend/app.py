from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/api/greet/<name>', methods=['GET'])
def greet_name(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)