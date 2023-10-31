import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('NAME', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
