from urllib import response
from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print("antes de la peticion")


@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


def not_found(error):
    return render_template('404.html'), 404


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/15P')
def phrasal():
    return render_template('content/15P.html')

@app.route('/15I')
def i15():
    return render_template('content/15I.html')

@app.route('/15S')
def s15():
    return render_template('content/15S.html')

@app.route('/50P')
def p50():
    return render_template('content/50P.html')

@app.route('/50I')
def i50():
    return render_template('content/50I.html')

@app.route('/50S')
def s50():
    return render_template('content/50S.html')

@app.route('/100P')
def p100():
    return render_template('content/100P.html')

@app.route('/100I')
def i100():
    return render_template('content/100I.html')

@app.route('/100S')
def s100():
    return render_template('content/100S.html')

@app.route('/test1')
def test1():
    return render_template('content/test1.html')

@app.route('/test2')
def test2():
    return render_template('content/test2.html')

@app.route('/test3')
def test3():
    return render_template('content/test3.html')

@app.route('/recursos')
def recursos():
    return render_template('content/recursos.html')

@app.route('/reco')
def reco():
    return render_template('content/reco.html')





def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "no"


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, not_found)
    app.run(debug=True)
