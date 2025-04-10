from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage/base.html')

@app.route('/sections/objective')
def objective():
    return render_template('sections/objective/base.html')

@app.route('/sections/methods')
def methods():
    return render_template('sections/methods/base.html')

@app.route('/sections/findings')
def findings():
    return render_template('sections/findings/base.html')

@app.route('/sections/data')
def data():
    return render_template('sections/data/base.html')

if __name__ == '__main__':
    app.run(debug=True)
