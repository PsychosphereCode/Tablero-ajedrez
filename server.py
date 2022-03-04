from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
    return render_template("index.html",fila=8,columna=8,color_uno='red',color_dos='black')


@app.route('/<int:x>')

def fila(x):
    return render_template("index.html",fila=x,columna=8,color_uno='red',color_dos='black')

@app.route('/<int:x>/<int:y>')

def fila_columna(x,y):
    return render_template("index.html",fila=x,columna=y,color_uno='red',color_dos='black')

@app.route('/<int:x>/<int:y>/<string:uno>')

def fila_columna_uno(x,y,uno):
    return render_template("index.html",fila=x,columna=y,color_uno=uno,color_dos='black')

@app.route('/<int:x>/<int:y>/<string:uno>/<string:dos>')

def fila_columna_dos(x,y,uno,dos):
    return render_template("index.html",fila=x,columna=y,color_uno=uno,color_dos=dos)

if __name__=="__main__":
    app.run(debug=True)