import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # Pega a variável de ambiente PORT ou usa 8080 por padrão
    port =  8080
    app.run(host='0.0.0.0', port=port)
