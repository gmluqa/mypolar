from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Cors (lax settings because testing in prod)
cors = CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

# localhost:5000 api test
@app.route('/')
def home():
    return "Hello world!"

# run in debug mode when launching `python3 app.py`
if __name__ == '__main__':
    app.run(debug=True)