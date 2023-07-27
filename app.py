from flask import Flask

# Criação da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')

def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Executa a aplicação no servidor local na porta 5000
    app.run()


# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/hello', methods=['GET'])
# def hello():
#     return jsonify(message="Hello, World!")

# if __name__ == '__main__':
#     app.run()
