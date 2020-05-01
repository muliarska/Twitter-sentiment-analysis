from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index1():
    """
    This function returns web page 'index.html'
    """
    return render_template("index.html")


@app.route("/statistic", methods=['POST'])
def index3():
    return render_template("example.html")


@app.errorhandler(404)
def invalid_route(e):
    """
    This function returns web page 'index.html'
    if error 404 is raised.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4245)
