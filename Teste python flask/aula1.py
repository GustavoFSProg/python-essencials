from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return "Olá Bucetinhas!!"


@app.route('/rota2')
def segundo():
    return "<H1>CUZÃO HEHEHE</H1>"

app.run()