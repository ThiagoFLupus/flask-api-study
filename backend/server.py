from src import app
from src.routes import route
from src import db

if __name__ == "__main__":
    print('Inicializando servidor na porta 5001...')
    app.run(host="0.0.0.0", debug=True)
else:
    print('Erro na inicialização do servidor!')
